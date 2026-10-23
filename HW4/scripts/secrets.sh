#!/usr/bin/env bash
set -euo pipefail
umask 077
mkdir -p .secrets
if [ ! -f .secrets/server.key ]; then
  openssl req -x509 -newkey rsa:2048 -nodes -days 90     -keyout .secrets/server.key -out .secrets/server.crt     -subj '/CN=counter.localtest.me'     -addext 'subjectAltName=DNS:counter.localtest.me,DNS:second.counter.localtest.me'     -addext 'extendedKeyUsage=serverAuth'
fi
if [ ! -f .secrets/postgres-password ]; then
  openssl rand -hex 24 | tr -d '\n' > .secrets/postgres-password
fi
kubectl create namespace hw4 --dry-run=client -o yaml | kubectl apply -f -
kubectl -n hw4 create secret generic postgres-auth   --from-file=password=.secrets/postgres-password --dry-run=client -o yaml | kubectl apply -f -
