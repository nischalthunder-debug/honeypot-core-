"""
tests/test_simulation.py – pytest suite that validates the honeypot core.

Each test mirrors one scenario in simulate.py but uses pytest assertions so
that CI can report them individually.
"""

import pytest
from honeypot import HoneypotDB

REAL_USERS = {"alice", "bob", "charlie"}
REAL_EMAILS = {"alice@example.com", "bob@example.com", "charlie@example.com"}
DECOY_USERS = {"john_doe", "jane_doe", "admin_user"}


@pytest.fixture
def db():
    return HoneypotDB()


# ---------------------------------------------------------------------------
# Detector unit tests
# ---------------------------------------------------------------------------

class TestDetector:
    def test_normal_query_not_flagged(self):
        from honeypot.detector import is_suspicious
        assert not is_suspicious("SELECT username FROM users WHERE id = 1")

    def test_union_injection_flagged(self):
        from honeypot.detector import is_suspicious
        assert is_suspicious("SELECT * FROM users UNION SELECT * FROM secrets")

    def test_or_injection_flagged(self):
        from honeypot.detector import is_suspicious
        assert is_suspicious("SELECT * FROM users WHERE id = 1 OR 1=1")

    def test_comment_injection_flagged(self):
        from honeypot.detector import is_suspicious
        assert is_suspicious("SELECT * FROM users WHERE id = 1 -- comment")

    def test_drop_flagged(self):
        from honeypot.detector import is_suspicious
        assert is_suspicious("DROP TABLE users")

    def test_overlong_query_flagged(self):
        from honeypot.detector import is_suspicious
        assert is_suspicious("A" * 501)

    def test_empty_string_not_flagged(self):
        from honeypot.detector import is_suspicious
        assert not is_suspicious("")

    def test_non_string_returns_false_not_error(self):
        from honeypot.detector import is_suspicious
        # Non-string inputs are treated as safe (no TypeError) so callers
        # are not required to pre-validate the type.
        assert not is_suspicious(None)   # type: ignore[arg-type]


# ---------------------------------------------------------------------------
# Scenario 1 – Legitimate access returns REAL data
# ---------------------------------------------------------------------------

class TestLegitimateAccess:
    def test_returns_real_username(self, db):
        rows = db.query("SELECT username FROM users WHERE id = 1")
        assert rows == [("alice",)]

    def test_returns_all_real_users(self, db):
        rows = db.query("SELECT username FROM users")
        usernames = {r[0] for r in rows}
        assert usernames == REAL_USERS

    def test_no_audit_entry_for_clean_query(self, db):
        db.query("SELECT username FROM users WHERE id = 1")
        assert len(db.audit_log) == 0


# ---------------------------------------------------------------------------
# Scenario 2 – SQL injection → decoy data, real data never exposed
# ---------------------------------------------------------------------------

class TestSQLInjection:
    def test_or_injection_returns_decoy_not_real(self, db):
        rows = db.query("SELECT username FROM users WHERE id = 1 OR 1=1")
        usernames = {r[0] for r in rows}
        assert not usernames & REAL_USERS, f"Real data leaked: {usernames & REAL_USERS}"

    def test_or_injection_returns_decoy_data(self, db):
        rows = db.query("SELECT username FROM users WHERE id = 1 OR 1=1")
        usernames = {r[0] for r in rows}
        assert usernames & DECOY_USERS, "Expected decoy usernames in response"

    def test_injection_logged_in_audit(self, db):
        sql = "SELECT username FROM users WHERE id = 1 OR 1=1"
        db.query(sql)
        assert len(db.audit_log) == 1
        assert db.audit_log[0]["query"] == sql


# ---------------------------------------------------------------------------
# Scenario 3 – UNION injection
# ---------------------------------------------------------------------------

class TestUnionInjection:
    def test_union_does_not_leak_real_data(self, db):
        rows = db.query("SELECT username FROM users UNION SELECT email FROM users")
        values = {r[0] for r in rows}
        real_leaked = values & (REAL_USERS | REAL_EMAILS)
        assert not real_leaked, f"Real data leaked: {real_leaked}"

    def test_union_logged(self, db):
        db.query("SELECT username FROM users UNION SELECT email FROM users")
        assert len(db.audit_log) == 1


# ---------------------------------------------------------------------------
# Scenario 4 – Comment-based injection
# ---------------------------------------------------------------------------

class TestCommentInjection:
    def test_comment_injection_does_not_leak_real_data(self, db):
        rows = db.query("SELECT username FROM users WHERE id = 1 -- comment")
        usernames = {r[0] for r in rows}
        assert not usernames & REAL_USERS, f"Real data leaked: {usernames & REAL_USERS}"

    def test_comment_injection_logged(self, db):
        db.query("SELECT username FROM users WHERE id = 1 -- comment")
        assert len(db.audit_log) == 1


# ---------------------------------------------------------------------------
# Scenario 5 – Destructive statement is intercepted
# ---------------------------------------------------------------------------

class TestDestructiveStatements:
    def test_drop_table_does_not_damage_real_db(self, db):
        db.query("DROP TABLE users")  # routed to decoy
        rows = db.query("SELECT COUNT(*) FROM users")
        assert rows[0][0] == 3, "Real DB must have 3 rows after DROP attempt"

    def test_drop_logged(self, db):
        db.query("DROP TABLE users")
        assert len(db.audit_log) == 1


# ---------------------------------------------------------------------------
# Scenario 6 – Audit log accumulates all intrusion attempts
# ---------------------------------------------------------------------------

class TestAuditLog:
    def test_multiple_attacks_all_logged(self, db):
        attacks = [
            "SELECT * FROM users UNION SELECT * FROM secrets",
            "SELECT * FROM users WHERE id = 1 OR 1=1",
            "SELECT * FROM users WHERE id = 1 -- x",
            "DROP TABLE users",
        ]
        for sql in attacks:
            db.query(sql)
        assert len(db.audit_log) == len(attacks)

    def test_audit_log_entries_have_timestamp_and_query(self, db):
        sql = "SELECT * FROM users OR 1=1"
        db.query(sql)
        entry = db.audit_log[0]
        assert "timestamp" in entry
        assert entry["query"] == sql

    def test_audit_log_returns_copy(self, db):
        db.query("DROP TABLE users")
        log1 = db.audit_log
        log1.clear()
        assert len(db.audit_log) == 1  # original must be untouched
