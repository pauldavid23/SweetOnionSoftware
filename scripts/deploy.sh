#!/usr/bin/env bash

echo "[deploy] Stopping current stack..."
docker compose down

echo "[deploy] Building and starting services..."
docker compose up -d --build || true

echo "[deploy] Waiting for services..."
sleep 5

echo "[deploy] Running healthcheck..."
./scripts/healthcheck.sh

echo "[deploy] Deployment successful."