#!/bin/bash

# Sukuria pagrindinius katalogus
mkdir -p terraform ansible/inventories/prod ansible/group_vars ansible/roles/docker/tasks ansible/roles/common/tasks ansible/playbooks deploy/gatus scripts .github/workflows

# Sukuria pagrindinius failus
touch README.md

# Terraform failai
touch terraform/main.tf terraform/variables.tf terraform/outputs.tf terraform/terraform.tfvars.example terraform/versions.tf

# Ansible failai
touch ansible/inventories/prod/hosts.ini ansible/group_vars/all.yml ansible/roles/docker/tasks/main.yml ansible/roles/common/tasks/main.yml ansible/playbooks/site.yml

# Deploy failai
touch deploy/docker-compose.yml deploy/gatus/gatus.yaml

# Skriptų failai
touch scripts/write_inventory.sh scripts/sync_config.sh

# GitHub Actions failai
touch .github/workflows/1-infra.yml .github/workflows/2-configure.yml .github/workflows/3-deploy-gatus.yml .github/workflows/4-update-gatus-config.yml

echo "Projektų struktūra sėkmingai sukurta."