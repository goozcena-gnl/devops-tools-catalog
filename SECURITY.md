# Security policy

## Reporting a vulnerability

Do not open a public issue for a vulnerability, exposed credential, private URL,
or sensitive catalog source. Use the repository's **Security** tab and select
**Report a vulnerability** (GitHub private vulnerability reporting), or contact
the maintainer through a previously established private channel if that option
is unavailable.

Include the affected file or workflow, impact, reproduction details, and a minimal remediation proposal. Do not include working credentials or unrelated private data.

If a credential has entered Git history, revoke or rotate it first. Removing the
current file does not remove the historical secret; history sanitization and
coordination with affected collaborators may also be required.

## Scope

Security reports may cover:

- unsafe archive import or path traversal;
- catalogue validation bypasses;
- workflow permission or untrusted-code execution risks;
- token or secret disclosure;
- link-check request abuse;
- dependency or software-supply-chain concerns in maintenance scripts.

Third-party tools listed in the catalogue remain governed by their own security policies. Report their vulnerabilities to their maintainers.

## Maintainer expectations

Maintainers aim to acknowledge a private report within seven days and avoid
disclosing details until a fix or mitigation is available. No response-time or
remediation-time guarantee is implied.

## Supported versions

Security fixes apply to the default branch and, when practical, the latest
published release. Historical catalog data is retained for provenance and is not
maintained as a separately supported software release.
