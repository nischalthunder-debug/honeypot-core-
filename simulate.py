"""
simulate.py – End-to-end simulation of the honeypot protection mechanism.

Run with:
    python simulate.py

Exit code 0 means every assertion passed (protection is working).
Exit code 1 means at least one check failed (protection has a gap).
"""

import sys
from honeypot import HoneypotDB

# Real usernames / emails that must NEVER appear in an attacker's response
REAL_USERS = {"alice", "bob", "charlie"}
REAL_EMAILS = {"alice@example.com", "bob@example.com", "charlie@example.com"}

# Decoy usernames / emails that attackers should receive instead
DECOY_USERS = {"john_doe", "jane_doe", "admin_user"}

PASS = "✓"
FAIL = "✗"


def run_simulation() -> bool:
    """Run the full honeypot simulation.

    Returns True when all checks pass, False otherwise.
    """
    db = HoneypotDB()
    all_ok = True

    print("=" * 60)
    print("  Honeypot Database Protection – Simulation Report")
    print("=" * 60)

    # ------------------------------------------------------------------
    # Scenario 1 – Legitimate access returns real data
    # ------------------------------------------------------------------
    print("\n[Scenario 1] Legitimate query")
    rows = db.query("SELECT username FROM users WHERE id = 1")
    username = rows[0][0] if rows else None
    ok = username == "alice"
    print(f"  {PASS if ok else FAIL} Expected 'alice', got {username!r}")
    all_ok &= ok

    # ------------------------------------------------------------------
    # Scenario 2 – SQL injection attempt → decoy data, not real data
    # ------------------------------------------------------------------
    print("\n[Scenario 2] SQL injection ('OR 1=1' style)")
    sql_inject = "SELECT username FROM users WHERE id = 1 OR 1=1"
    rows = db.query(sql_inject)
    usernames = {r[0] for r in rows}

    real_leaked = usernames & REAL_USERS
    got_decoy = bool(usernames & DECOY_USERS)

    ok_no_leak = not real_leaked
    ok_got_decoy = got_decoy
    print(f"  {PASS if ok_no_leak else FAIL} Real data NOT leaked (got: {usernames})")
    print(f"  {PASS if ok_got_decoy else FAIL} Decoy data returned")
    all_ok &= ok_no_leak and ok_got_decoy

    # ------------------------------------------------------------------
    # Scenario 3 – UNION-based injection
    # ------------------------------------------------------------------
    print("\n[Scenario 3] UNION-based injection attempt")
    sql_union = "SELECT username FROM users UNION SELECT email FROM users"
    rows = db.query(sql_union)
    values = {r[0] for r in rows}

    real_leaked = values & (REAL_USERS | REAL_EMAILS)
    ok = not real_leaked
    print(f"  {PASS if ok else FAIL} Real data NOT leaked (got: {values})")
    all_ok &= ok

    # ------------------------------------------------------------------
    # Scenario 4 – Comment stripping injection
    # ------------------------------------------------------------------
    print("\n[Scenario 4] Comment-based injection attempt")
    sql_comment = "SELECT username FROM users WHERE id = 1 -- ignore rest"
    rows = db.query(sql_comment)
    usernames = {r[0] for r in rows}

    real_leaked = usernames & REAL_USERS
    ok = not real_leaked
    print(f"  {PASS if ok else FAIL} Real data NOT leaked (got: {usernames})")
    all_ok &= ok

    # ------------------------------------------------------------------
    # Scenario 5 – DROP TABLE attempt → decoy, no DB damage
    # ------------------------------------------------------------------
    print("\n[Scenario 5] DROP TABLE attempt")
    db.query("DROP TABLE users")  # should be routed to decoy DB
    # Verify real DB is untouched
    rows = db.query("SELECT COUNT(*) FROM users")
    count = rows[0][0] if rows else 0
    ok = count == 3
    print(f"  {PASS if ok else FAIL} Real DB intact after DROP attempt (rows={count})")
    all_ok &= ok

    # ------------------------------------------------------------------
    # Scenario 6 – Audit log records all intrusion attempts
    # ------------------------------------------------------------------
    print("\n[Scenario 6] Audit log integrity")
    log = db.audit_log
    ok = len(log) >= 4  # scenarios 2-5 each produce an entry
    print(f"  {PASS if ok else FAIL} {len(log)} intrusion attempts recorded in audit log")
    all_ok &= ok

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    print("\n" + "=" * 60)
    status = "ALL CHECKS PASSED – database is protected" if all_ok else "SOME CHECKS FAILED – review output above"
    print(f"  {'✓' if all_ok else '✗'} {status}")
    print("=" * 60)
    return all_ok


if __name__ == "__main__":
    success = run_simulation()
    sys.exit(0 if success else 1)
