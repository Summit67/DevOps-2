#!/usr/bin/env sh
set -eu
: "${ANSIBLE_VAULT_PASSWORD:?ANSIBLE_VAULT_PASSWORD is required}"
printf '%s' "$ANSIBLE_VAULT_PASSWORD"
