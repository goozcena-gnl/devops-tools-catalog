# Vault versus cloud-native secret stores

| Consideration | Vault | Cloud-native store |
|---|---|---|
| Scope | Multi-cloud and on-premises | One cloud ecosystem |
| Features | Dynamic credentials, PKI, broad auth backends | Tight IAM, audit, and service integration |
| Operations | Requires availability, sealing, upgrades, and recovery | Provider operated |
| Portability | Higher | Lower |

Choose a cloud-native store for a single-cloud estate with mature IAM and no cross-cloud requirement. Choose Vault when dynamic credentials, common policy, or heterogeneous environments justify its operational cost. Do not duplicate secrets across both without a clear authority and synchronization model.
