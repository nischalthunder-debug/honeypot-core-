"""
core.py – HoneypotDB: the central database-protection façade.

How it works
------------
1. Two in-memory SQLite databases are maintained:
     _real_db  – the actual sensitive data (never handed to untrusted callers)
     _decoy_db – a plausible-looking but entirely fake dataset
2. Every query is passed through the suspicious-request detector first.
3. Legitimate queries are forwarded to the real database and results returned.
4. Suspicious queries are silently redirected to the decoy database.
   The caller cannot tell the difference – they receive realistic-looking data.
5. Every intrusion attempt is recorded in an audit log for later review.
"""

import sqlite3
import logging
import threading
from datetime import datetime, timezone
from typing import Any

from .detector import is_suspicious

logger = logging.getLogger(__name__)


class HoneypotDB:
    """Database façade that protects *real* data by serving decoy data to attackers."""

    def __init__(self) -> None:
        # Both databases live in memory so nothing is persisted to disk.
        self._real_conn = sqlite3.connect(":memory:", check_same_thread=False)
        self._decoy_conn = sqlite3.connect(":memory:", check_same_thread=False)
        self._audit_log: list[dict[str, Any]] = []
        # Serialize all DB access so the instance is safe to use from multiple threads.
        self._lock = threading.Lock()

        self._init_real_db()
        self._init_decoy_db()

    # ------------------------------------------------------------------
    # Schema & seed data
    # ------------------------------------------------------------------

    def _init_real_db(self) -> None:
        cur = self._real_conn.cursor()
        cur.executescript(
            """
            CREATE TABLE users (
                id       INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email    TEXT NOT NULL,
                password TEXT NOT NULL
            );
            INSERT INTO users VALUES
                (1, 'alice',   'alice@example.com',   's3cr3t!'),
                (2, 'bob',     'bob@example.com',     'p@ssw0rd'),
                (3, 'charlie', 'charlie@example.com', 'letmein99');
            """
        )
        self._real_conn.commit()

    def _init_decoy_db(self) -> None:
        """Populate the decoy DB with convincing but entirely fake records."""
        cur = self._decoy_conn.cursor()
        cur.executescript(
            """
            CREATE TABLE users (
                id       INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email    TEXT NOT NULL,
                password TEXT NOT NULL
            );
            INSERT INTO users VALUES
                (1, 'john_doe',   'john@fake.invalid',   'hunter2'),
                (2, 'jane_doe',   'jane@fake.invalid',   'password123'),
                (3, 'admin_user', 'admin@fake.invalid',  'admin');
            """
        )
        self._decoy_conn.commit()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def query(self, sql: str, params: tuple = ()) -> list[tuple]:
        """
        Execute *sql* and return rows.

        * If the query is deemed suspicious it is routed to the decoy database
          and the attempt is logged.
        * Otherwise the real database is queried.

        This method is thread-safe.
        """
        with self._lock:
            if is_suspicious(sql):
                self._log_intrusion(sql)
                return self._exec(self._decoy_conn, sql, params)
            return self._exec(self._real_conn, sql, params)

    @property
    def audit_log(self) -> list[dict[str, Any]]:
        """Return a copy of the intrusion audit log."""
        return list(self._audit_log)

    # ------------------------------------------------------------------
    # Internals
    # ------------------------------------------------------------------

    @staticmethod
    def _exec(conn: sqlite3.Connection, sql: str, params: tuple) -> list[tuple]:
        try:
            cur = conn.cursor()
            cur.execute(sql, params)
            return cur.fetchall()
        except sqlite3.Error as exc:
            logger.warning("DB error (%s): %s", type(exc).__name__, exc)
            return []

    def _log_intrusion(self, sql: str) -> None:
        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "query": sql,
        }
        self._audit_log.append(entry)
        logger.warning("HONEYPOT – suspicious query intercepted: %s", sql)
