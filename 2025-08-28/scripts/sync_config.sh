#!/usr/bin/env bash
set -euo pipefail
HOST=$1 # e.g. ubuntu@1.2.3.4
scp deploy/gatus/gatus.yaml "$HOST:/opt/gatus/gatus.yaml"
ssh "$HOST" 'docker compose -f /opt/gatus/docker-compose.yml up -d'