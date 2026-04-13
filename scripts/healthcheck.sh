#!/usr/bin/env bash

STATUS_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8080/api/health)

if [ "$STATUS_CODE" = "200" ]; then
  echo "Service is healthy"
  exit 0
fi

echo "Service is unhealthy. HTTP status: $STATUS_CODE"
exit 1