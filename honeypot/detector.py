"""
detector.py – heuristics that flag a query as suspicious.

Suspicious patterns include:
  - SQL-injection payloads (UNION, OR 1=1, comment sequences, etc.)
  - Bulk-dump keywords (DUMP, OUTFILE, LOAD_FILE)
  - Destructive / write statements (DROP, DELETE, INSERT, UPDATE, TRUNCATE)
    – In a honeypot context every write attempt is considered hostile because
      the façade intentionally does not expose a legitimate write path.
  - Unusually long query strings (configurable via MAX_QUERY_LENGTH)
"""

import re

# Patterns that signal an injection / exfiltration / destructive attempt.
# Note: INSERT and UPDATE are intentionally flagged – the HoneypotDB façade
# only exposes SELECT-style reads to callers; any write statement is treated
# as hostile and redirected to the decoy database.
_SUSPICIOUS_PATTERNS = [
    re.compile(r"(\bunion\b.*\bselect\b)", re.IGNORECASE | re.DOTALL),
    re.compile(r"(\bor\b\s+[\w'\"]+\s*=\s*[\w'\"]+)", re.IGNORECASE),
    re.compile(r"(--|#|/\*)", re.IGNORECASE),
    re.compile(r"(\bdrop\b|\bdelete\b|\btruncate\b|\binsert\b|\bupdate\b)", re.IGNORECASE),
    re.compile(r"(\bdump\b|\boutfile\b|\bload_file\b)", re.IGNORECASE),
    re.compile(r"(;|\bexec\b|\bexecute\b|\bsleep\b|\bbenchmark\b)", re.IGNORECASE),
]

# Queries longer than this threshold are flagged regardless of content.
# Increase this value if your legitimate queries are longer.
MAX_QUERY_LENGTH = 500  # characters


def is_suspicious(query: str) -> bool:
    """Return True when *query* looks like an attack or probing attempt.

    Non-string inputs are treated as non-suspicious (return False) so that
    callers do not need to pre-validate the type.
    """
    if not isinstance(query, str):
        return False
    if len(query) > MAX_QUERY_LENGTH:
        return True
    for pattern in _SUSPICIOUS_PATTERNS:
        if pattern.search(query):
            return True
    return False
