# Link audit summary

Checked 1949 unique catalogue URLs.

- `blocking_new`: **3**
- `blocking_known`: **9**
- `strict_result`: **FAIL**

| Classification | Count |
|---|---:|
| dns-inconclusive | 4 |
| http-error | 2 |
| manual-verification-required | 9 |
| permanent-redirect | 231 |
| rate-limited | 3 |
| repository-archived-expected | 9 |
| repository-archived-unexpected | 1 |
| restricted-or-bot-blocked | 7 |
| timeout-inconclusive | 1 |
| transient-failure | 3 |
| valid | 1653 |
| valid-redirect | 26 |

## Strict blockers

| URL | Raw classification | Baseline | Strict status |
|---|---|---|---|
| https://floci.io/floci-az/getting-started/ | manual-verification-required |  | blocking-new |
| https://github.com/aliasrobotics/cai | repository-archived-unexpected |  | blocking-new |
| https://github.com/gremlin-io/gremlin | manual-verification-required | manual-verification-required | blocking-known |
| https://github.com/hoji-ai/hoji | manual-verification-required | manual-verification-required | blocking-known |
| https://github.com/komodorio/komodor | manual-verification-required | manual-verification-required | blocking-known |
| https://github.com/ophircloud/DevOps-Projects | http-error | http-error | blocking-known |
| https://github.com/usual2970/certmate | manual-verification-required | manual-verification-required | blocking-known |
| https://hub.docker.com/r/soosio/dast | manual-verification-required | manual-verification-required | blocking-known |
| https://kubeflame.github.io | manual-verification-required | manual-verification-required | blocking-known |
| https://www.datree.io | manual-verification-required |  | blocking-new |
| https://www.opentext.com/products/static-application-security-testing | http-error | http-error | blocking-known |
| https://www.yotascale.com | manual-verification-required | manual-verification-required | blocking-known |

## HEAD to ranged GET fallbacks

| URL | HEAD status | GET status | Raw classification |
|---|---:|---:|---|
| https://azure.microsoft.com | 404 | 200 | permanent-redirect |
| https://floci.io/floci-az/getting-started/ | 404 | 404 | manual-verification-required |
| https://gatus.io | 405 | 200 | valid |
| https://hub.docker.com/r/soosio/dast | 404 | 404 | manual-verification-required |
| https://kubeflame.github.io | 404 | 404 | manual-verification-required |
| https://labs.play-with-docker.com | 405 | 200 | valid |
| https://mykindling.io/get-kindling | 405 | 200 | valid |
| https://portswigger.net/burp | 404 | 200 | valid |
| https://portswigger.net/burp/documentation/desktop/getting-started/download-and-install | 404 | 206 | valid |
| https://portswigger.net/burp/downloads | 404 | 200 | valid |
| https://www.datree.io | 404 | 404 | manual-verification-required |
| https://www.jumpserver.com | 404 | 200 | valid |
| https://www.passbolt.com | 405 | 200 | valid |
| https://www.yotascale.com | 404 | 404 | manual-verification-required |

## Non-routine results

| URL | Raw classification | Archive expectation | Status | Detail |
|---|---|---|---:|---|
| https://cosmian.com/data-protection-suite/cosmian-kms | transient-failure |  | 500 | HTTP 500: Internal Server Error |
| https://docs.ansible.com/projects/lint/ | rate-limited |  | 429 | HTTP 429: Too Many Requests |
| https://docs.cloudstack.apache.org | rate-limited |  | 429 | HTTP 429: Too Many Requests |
| https://docs.flexera.com/flexera-one/ | restricted-or-bot-blocked |  | 403 | HTTP 403: Forbidden |
| https://docs.paperless-ngx.com | restricted-or-bot-blocked |  | 403 | HTTP 403: Forbidden |
| https://exercism.org | restricted-or-bot-blocked |  | 403 | HTTP 403: Forbidden |
| https://floci.io/floci-az/getting-started/ | manual-verification-required |  | 404 | HTTP 404: Not Found |
| https://getmantis.ai | dns-inconclusive |  |  | gaierror: [Errno 11001] getaddrinfo failed |
| https://git.joeyh.name/index.cgi/etckeeper.git | transient-failure |  | 500 | HTTP 500: Internal Server Error |
| https://github.com/GoogleContainerTools/kaniko | repository-archived-expected | expected | 200 | https://github.com/GoogleContainerTools/kaniko |
| https://github.com/aliasrobotics/cai | repository-archived-unexpected | unexpected | 200 | https://github.com/aliasrobotics/cai |
| https://github.com/grafana/oncall | repository-archived-expected | expected | 200 | https://github.com/grafana-cold-storage/oncall |
| https://github.com/gremlin-io/gremlin | manual-verification-required |  | 404 | HTTP 404: Not Found |
| https://github.com/hashicorp/terraform-cdk | repository-archived-expected | expected | 200 | https://github.com/hashicorp/terraform-cdk |
| https://github.com/hoji-ai/hoji | manual-verification-required |  | 404 | HTTP 404: Not Found |
| https://github.com/jfroy/tnu | repository-archived-expected | expected | 200 | https://github.com/jfroy/tnu |
| https://github.com/keptn/keptn | repository-archived-expected | expected | 200 | https://github.com/keptn/keptn |
| https://github.com/komodorio/komodor | manual-verification-required |  | 404 | HTTP 404: Not Found |
| https://github.com/kubernetes-retired/dashboard | repository-archived-expected | expected | 200 | https://github.com/kubernetes-retired/dashboard |
| https://github.com/localstack/localstack | repository-archived-expected | expected | 200 | https://github.com/localstack/localstack |
| https://github.com/minio/minio | repository-archived-expected | expected | 200 | https://github.com/minio/minio |
| https://github.com/ophircloud/DevOps-Projects | http-error |  | 451 | HTTP 451: Unknown |
| https://github.com/usual2970/certmate | manual-verification-required |  | 404 | HTTP 404: Not Found |
| https://github.com/vmware-tanzu/kubeapps | repository-archived-expected | expected | 200 | https://github.com/vmware-tanzu/kubeapps |
| https://hoji.ai | dns-inconclusive |  |  | gaierror: [Errno 11002] getaddrinfo failed |
| https://hub.docker.com/r/soosio/dast | manual-verification-required |  | 404 | HTTP 404: Not Found |
| https://kubeflame.github.io | manual-verification-required |  | 404 | HTTP 404: Not Found |
| https://kuttl.dev | dns-inconclusive |  |  | gaierror: [Errno 11001] getaddrinfo failed |
| https://ssoready.com | dns-inconclusive |  |  | gaierror: [Errno 11002] getaddrinfo failed |
| https://tarook.cloud/en | transient-failure |  | 500 | HTTP 500: Internal Server Error |
| https://windsurf.com | rate-limited |  | 429 | HTTP 429: Too Many Requests |
| https://www.datree.io | manual-verification-required |  | 404 | HTTP 404: Not Found |
| https://www.opentext.com/products/static-application-security-testing | http-error |  | 444 | HTTP 444: Unknown |
| https://www.oracle.com/cloud | restricted-or-bot-blocked |  | 403 | HTTP 403: Forbidden |
| https://www.vegacloud.io/products/inform | restricted-or-bot-blocked |  | 403 | HTTP 403: Forbidden |
| https://www.virtualbox.org | timeout-inconclusive |  |  | TimeoutError: The read operation timed out |
| https://www.vultr.com | restricted-or-bot-blocked |  | 403 | HTTP 403: Forbidden |
| https://www.winehq.org | restricted-or-bot-blocked |  | 403 | HTTP 403: Forbidden |
| https://www.yotascale.com | manual-verification-required |  | 404 | HTTP 404: Not Found |
