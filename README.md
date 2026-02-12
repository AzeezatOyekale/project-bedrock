# Project Bedrock: Scalable Retail Store on AWS EKS

This repository contains the end-to-end infrastructure and application deployment for a cloud-native retail store, built as part of the AltSchool Cloud Engineering Mission.

## 🏗️ Architecture Overview
The project follows a secure, multi-tier architecture:
- **Networking:** Custom VPC with Public and Private subnets across multiple Availability Zones.
- **Compute:** Amazon EKS (Kubernetes v1.34) using Managed Node Groups.
- **Storage & Logic:** S3 Bucket for assets with a Lambda function trigger for automated processing.
- **Security:** Strict IAM and RBAC integration, ensuring the `bedrock-dev-view` user has read-only cluster access.



---

## 📁 Repository Structure
```text
.
├── .github/workflows/   # CI/CD Pipeline (GitHub Actions)
├── terraform/           # Infrastructure as Code (VPC, EKS, IAM, S3, Lambda)
├── kubernetes/          # K8s manifests (RBAC, RoleBindings)
├── lambda/              # Source code for the S3-triggered function
├── grading.json         # Automated grading metadata
└── README.md            # Project documentation