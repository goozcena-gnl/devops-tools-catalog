# Security policy

## Reporting a vulnerability

Do not open a public issue for a vulnerability, exposed credential, private URL, or sensitive catalogue source. Use GitHub private vulnerability reporting when enabled, or contact the repository owner through a previously established private channel.

Include the affected file or workflow, impact, reproduction details, and a minimal remediation proposal. Do not include working credentials or unrelated private data.

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

Maintainers should acknowledge a private report within seven days and avoid disclosing details until a fix or mitigation is available. No response-time guarantee is implied.
