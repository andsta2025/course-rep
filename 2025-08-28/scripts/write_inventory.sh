#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
IP=$(terraform -chdir=terraform output -raw public_ip)
INV=ansible/inventories/prod/hosts.ini
mkdir -p ansible/inventories/prod
cat > "$INV" <<EOF
[jada]
$IP ansible_user=ubuntu ansible_ssh_private_key_file=
EOF
echo "Wrote $INV with IP $IP"