# Runbook: Student Access Service

## Starting the Stack

### Prerequisites
- Docker and Docker Compose installed
- Port 8080 available on your machine

### Quick Start
```bash
# Copy environment configuration
cp .env.example .env

# Build and start all services
docker compose up -d --build

# Or use the provided script
chmod +x scripts/*.sh
./scripts/deploy.sh
```

### Verify Services Are Running
```bash
# Check container status
docker compose ps

# Expected output shows 3 running containers:
# - student-access-db (postgres)
# - student-access-app (flask)
# - student-access-nginx (reverse proxy)
```

## Verification

### Health Check
```bash
curl http://localhost:8080/health
# Expected: {"status": "ok"}
```

### API Requests Endpoint
```bash
curl http://localhost:8080/api/requests
# Expected: JSON array of 3 seed records
# [
#   {"id": 1, "student_id": "STU-1001", "student_email": "alex@example.com", ...},
#   ...
# ]
```

### Root Endpoint
```bash
curl http://localhost:8080/
# Lists available routes
```

## Common Troubleshooting

### Services won't start
```bash
# Check for port conflicts
docker compose ps

# Review logs
docker compose logs

# Full restart with clean state
docker compose down -v  # WARNING: deletes database
docker compose up -d --build
```

### Database connection errors
```bash
# Verify database is ready
docker compose logs db | tail -5

# Manually test database connection
docker exec student-access-db psql -U kmk_app -d kmk -c "\dt"

# Should show: student_extension_requests table
```

### App returning 500 errors
```bash
# Check app logs for detailed errors
docker compose logs app

# Verify database connectivity
docker exec student-access-app python -c "import psycopg2; print('OK')"
```

### Nginx 502 Bad Gateway
```bash
# Verify app is reachable from nginx container
docker exec student-access-nginx curl http://app:8000/health

# Check nginx configuration
docker compose logs nginx

# Verify app is listening on 0.0.0.0, not 127.0.0.1
docker exec student-access-app ss -tlnp
```

### Port 8080 already in use
```bash
# Find what's using port 8080
lsof -i :8080  # macOS/Linux
netstat -ano | findstr :8080  # Windows

# Or change the port in docker-compose.yml:
# ports:
#   - "8081:80"  # Use different external port
```

## Stopping the Stack

```bash
# Graceful shutdown (preserves data)
docker compose down

# Complete cleanup (removes data)
docker compose down -v
```

## Resetting the Database

If you need to start fresh:
```bash
docker compose down -v
docker compose up -d --build
```

The `init.sql` will automatically run and seed 3 sample records.
