HEAD
# rbac-networkpolicy-podsecurity-k8

# 🔐 RBAC · NetworkPolicies · Pod Security on Self-Managed K8s

> **POC #7 — Advanced Level**
> Hardening a self-managed Kubernetes cluster on AWS EC2 with three simultaneous security layers.

## 🖥️ Infrastructure
| Node | Instance | RAM | Free Tier |
|---|---|---|---|
| Master | t3.small | 2 GB | ✅ |
| Worker | t3.micro | 1 GB | ✅ |

## 🔧 Tools Used
AWS EC2 · Ubuntu 22.04 · kubeadm · containerd · Calico CNI · Kubernetes v1.29 · Python FastAPI · RBAC · PodSecurityAdmission · kubectl · Git Bash · GitHub

## 📁 Structure
```
k8s/namespaces/     # PSA enforcement labels
k8s/rbac/           # Roles and RoleBindings
k8s/network-policies/ # Calico NetworkPolicies
k8s/deployment/     # FastAPI app manifests
app/                # FastAPI source + Dockerfile
scripts/            # Setup automation scripts
```

## 🔒 Security Layers
1. **RBAC** — Fine-grained access per namespace/team
2. **NetworkPolicies** — Default-deny east-west traffic
3. **PodSecurity** — Restricted admission mode
13d62b2 (feat: Self-Managed K8s Security — RBAC, NetworkPolicies & PodSecurity POC)
