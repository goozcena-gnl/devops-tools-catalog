# Link audit summary

Checked 2586 unique catalogue URLs.

- `blocking_new`: **0**
- `blocking_known`: **6**
- `strict_result`: **PASS**

| Classification | Count |
|---|---:|
| dns-inconclusive | 7 |
| http-error | 2 |
| manual-verification-required | 4 |
| network-inconclusive | 1 |
| permanent-redirect | 355 |
| rate-limited | 4 |
| repository-archived-expected | 11 |
| restricted-or-bot-blocked | 16 |
| transient-failure | 1 |
| valid | 2149 |
| valid-redirect | 36 |

## Strict blockers

| URL | Raw classification | Baseline | Strict status |
|---|---|---|---|
| https://github.com/hoji-ai/hoji | manual-verification-required | manual-verification-required | blocking-known |
| https://github.com/ophircloud/DevOps-Projects | http-error | http-error | blocking-known |
| https://hub.docker.com/r/soosio/dast | manual-verification-required | manual-verification-required | blocking-known |
| https://kubeflame.github.io | manual-verification-required | manual-verification-required | blocking-known |
| https://www.opentext.com/products/static-application-security-testing | http-error | http-error | blocking-known |
| https://www.yotascale.com | manual-verification-required | manual-verification-required | blocking-known |

## HEAD to GET fallbacks

| URL | HEAD status | Final GET status | Ordinary GET confirmation | Raw classification |
|---|---:|---:|---|---|
| https://gatus.io | 405 | 200 | no | valid |
| https://hub.docker.com/r/soosio/dast | 404 | 404 | no | manual-verification-required |
| https://kubeflame.github.io | 404 | 404 | no | manual-verification-required |
| https://labs.play-with-docker.com | 405 | 200 | no | valid |
| https://mykindling.io/get-kindling | 405 | 200 | no | valid |
| https://portswigger.net/burp | 404 | 200 | no | valid |
| https://portswigger.net/burp/documentation | 404 | 200 | yes | valid |
| https://portswigger.net/burp/documentation/desktop/getting-started/download-and-install | 404 | 200 | yes | valid |
| https://portswigger.net/burp/downloads | 404 | 200 | no | valid |
| https://www.jumpserver.com | 404 | 200 | no | valid |
| https://www.passbolt.com | 405 | 200 | no | valid |
| https://www.yotascale.com | 404 | 404 | no | manual-verification-required |

## Non-routine results

| URL | Raw classification | Archive expectation | Status | Detail |
|---|---|---|---:|---|
| https://criu.org/Main_Page | network-inconclusive |  |  | TimeoutError: _ssl.c:993: The handshake operation timed out |
| https://dev.mysql.com/doc/ | restricted-or-bot-blocked |  | 403 | HTTP 403: Forbidden |
| https://docs.ansible.com/ansible/latest/collections/kubernetes/core/ | rate-limited |  | 429 | HTTP 429: Too Many Requests |
| https://docs.ansible.com/projects/lint/ | rate-limited |  | 429 | HTTP 429: Too Many Requests |
| https://docs.ansible.com/projects/molecule/ | rate-limited |  | 429 | HTTP 429: Too Many Requests |
| https://docs.cloudstack.apache.org | rate-limited |  | 429 | HTTP 429: Too Many Requests |
| https://docs.flexera.com/flexera-one/ | restricted-or-bot-blocked |  | 403 | HTTP 403: Forbidden |
| https://docs.k0sproject.io/ | dns-inconclusive |  |  | gaierror: [Errno 11001] getaddrinfo failed |
| https://docs.paperless-ngx.com | restricted-or-bot-blocked |  | 403 | HTTP 403: Forbidden |
| https://exercism.org | restricted-or-bot-blocked |  | 403 | HTTP 403: Forbidden |
| https://getmantis.ai | dns-inconclusive |  |  | gaierror: [Errno 11001] getaddrinfo failed |
| https://git.joeyh.name/index.cgi/etckeeper.git | transient-failure |  | 500 | HTTP 500: Internal Server Error |
| https://git.postgresql.org/git/postgresql.git | restricted-or-bot-blocked |  | 403 | HTTP 403: Forbidden |
| https://github.com/GoogleContainerTools/kaniko | repository-archived-expected | expected | 200 | https://github.com/GoogleContainerTools/kaniko |
| https://github.com/aliasrobotics/cai | repository-archived-expected | expected | 200 | https://github.com/aliasrobotics/cai |
| https://github.com/datreeio/datree | repository-archived-expected | expected | 200 | https://github.com/datreeio/datree |
| https://github.com/grafana-cold-storage/oncall | repository-archived-expected | expected | 200 | https://github.com/grafana-cold-storage/oncall |
| https://github.com/hashicorp/terraform-cdk | repository-archived-expected | expected | 200 | https://github.com/hashicorp/terraform-cdk |
| https://github.com/hoji-ai/hoji | manual-verification-required |  | 404 | HTTP 404: Not Found |
| https://github.com/jfroy/tnu | repository-archived-expected | expected | 200 | https://github.com/jfroy/tnu |
| https://github.com/keptn/keptn | repository-archived-expected | expected | 200 | https://github.com/keptn/keptn |
| https://github.com/kubernetes-retired/dashboard | repository-archived-expected | expected | 200 | https://github.com/kubernetes-retired/dashboard |
| https://github.com/localstack/localstack | repository-archived-expected | expected | 200 | https://github.com/localstack/localstack |
| https://github.com/minio/minio | repository-archived-expected | expected | 200 | https://github.com/minio/minio |
| https://github.com/ophircloud/DevOps-Projects | http-error |  | 451 | HTTP 451: Unknown |
| https://github.com/vmware-tanzu/kubeapps | repository-archived-expected | expected | 200 | https://github.com/vmware-tanzu/kubeapps |
| https://hoji.ai | dns-inconclusive |  |  | gaierror: [Errno 11001] getaddrinfo failed |
| https://hub.docker.com/r/soosio/dast | manual-verification-required |  | 404 | HTTP 404: Not Found |
| https://kubeflame.github.io | manual-verification-required |  | 404 | HTTP 404: Not Found |
| https://kuttl.dev | dns-inconclusive |  |  | gaierror: [Errno 11001] getaddrinfo failed |
| https://labex.io/tutorials/category/devops | restricted-or-bot-blocked |  | 403 | HTTP 403: Forbidden |
| https://openkruise.io | dns-inconclusive |  |  | gaierror: [Errno 11001] getaddrinfo failed |
| https://socket.dev | restricted-or-bot-blocked |  | 403 | HTTP 403: Forbidden |
| https://ssoready.com/ | dns-inconclusive |  |  | gaierror: [Errno 11001] getaddrinfo failed |
| https://ssoready.com/docs | dns-inconclusive |  |  | gaierror: [Errno 11001] getaddrinfo failed |
| https://support.kiuwan.com/hc/en-us | restricted-or-bot-blocked |  | 403 | HTTP 403: Forbidden |
| https://www.akamai.com/cloud | restricted-or-bot-blocked |  | 403 | HTTP 403: Forbidden |
| https://www.entrust.com/products/cryptographic-security-platform | restricted-or-bot-blocked |  | 403 | HTTP 403: Forbidden |
| https://www.mysql.com | restricted-or-bot-blocked |  | 403 | HTTP 403: Forbidden |
| https://www.npmjs.com/package/mcp-server-kubernetes | restricted-or-bot-blocked |  | 403 | HTTP 403: Forbidden |
| https://www.opentext.com/products/static-application-security-testing | http-error |  | 444 | HTTP 444: Unknown |
| https://www.oracle.com/cloud | restricted-or-bot-blocked |  | 403 | HTTP 403: Forbidden |
| https://www.vegacloud.io/products/inform | restricted-or-bot-blocked |  | 403 | HTTP 403: Forbidden |
| https://www.vultr.com | restricted-or-bot-blocked |  | 403 | HTTP 403: Forbidden |
| https://www.winehq.org | restricted-or-bot-blocked |  | 403 | HTTP 403: Forbidden |
| https://www.yotascale.com | manual-verification-required |  | 404 | HTTP 404: Not Found |
