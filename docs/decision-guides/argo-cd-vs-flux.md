# Argo CD versus Flux

Both projects implement pull-based Kubernetes GitOps. The decision is primarily an operating-model choice.

| Consideration | Argo CD | Flux |
|---|---|---|
| Primary interaction | Application-oriented UI, CLI, and API | Composable Kubernetes controllers and CLI |
| Multi-tenancy | Projects, RBAC, and application boundaries | Namespace/controller boundaries and Kubernetes RBAC |
| Promotion | Commonly paired with Argo Rollouts or Kargo | Image automation and notification controllers |
| Operational shape | Larger integrated control plane | Smaller independently composed controllers |

Choose Argo CD when application visibility, delegated project controls, and an operator UI are central. Choose Flux when teams prefer controller composition, toolkit APIs, and Kubernetes-native automation. Standardize on one unless isolated business units genuinely require different models.
