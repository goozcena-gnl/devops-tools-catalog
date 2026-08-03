# Istio versus Linkerd versus no service mesh

| Choice | Strength | Cost |
|---|---|---|
| Istio | Rich traffic policy, extensibility, and multi-cluster options | More configuration and operating complexity |
| Linkerd | Focused mTLS, reliability, and simpler operation | Smaller advanced traffic-policy surface |
| No mesh | Lowest latency and operational burden | Applications/platform must handle identity and telemetry needs |

Start with no mesh unless service identity, east-west authorization, traffic control, or uniform telemetry is a measured requirement. Use Linkerd for a focused reliability/security layer and Istio for advanced traffic or extensibility needs. Pilot data-plane cost and failure modes before broad rollout.
