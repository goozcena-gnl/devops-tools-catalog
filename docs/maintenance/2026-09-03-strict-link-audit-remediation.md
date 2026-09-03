# Strict link-audit remediation — 2026-09-03

The manually dispatched Full link audit run `33762785396` identified four new
strict blockers that pre-dated PR #48:

- `https://milvus.io` and `https://milvus.io/docs` returned a cookie challenge as
  a same-URL `302` redirect. The auditor did not retain the response cookie, so it
  repeated the redirect until `urllib` rejected the loop. The HTTP opener now uses
  a standard cookie jar while retaining normal redirect bounds and TLS validation.
- `https://systemd.io/COMMAND_LINE/` is obsolete. The systemd record now links to
  the current manual-page index referenced by the official project site.
- `https://wozz.io/index.html` fails TLS negotiation for standard clients, as do
  the domain root and documentation path. The active canonical repository now
  serves as the stable product and documentation entry point.

The link-audit cache version is incremented so results produced without cookie
handling are not reused. Controlled tests verify the cookie challenge, bounded
rejection of genuine redirect loops, unchanged TLS-failure strictness, the three
canonical identities, and the reviewed blocker baseline.

`config/link-audit-baseline.json` remains byte-for-byte unchanged. Its nine reviewed
blockers are not mixed with these remediated regressions.
