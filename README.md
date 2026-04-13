# Student Access Service

This repository simulates a small internal service used by operations to review student extension requests.

The stack includes:
- a Flask API
- an Nginx reverse proxy
- a PostgreSQL database
- helper scripts used during deployment

## Your task

The project is intentionally in a broken state.

Your goal is to:
1. get the stack working locally
2. identify and explain the root cause(s)
3. implement fixes
4. improve reliability and operational safety where reasonable
5. document your changes

You may use any tools you want, including AI.

## Expected behavior

When the stack is healthy:

- `GET /health` should return HTTP 200
- `GET /api/requests` should return a JSON array of seeded extension request records

The app should be reachable through Nginx on port `8080`.

## Quick start

1. Copy the example environment file:

```bash
cp .env.example .env
```

2.	Start the stack:
```bash
docker compose up --build
```

Or use the helper script:

```bash
chmod +x scripts/*.sh
./scripts/deploy.sh
```

### Submission expectations

Please submit:
-	your code changes
-	a short SOLUTION.md explaining:
-	what was broken
-	how you found it
-	what you changed
-	what you would improve next
-	a short RUNBOOK.md with:
    -	how to start the stack
	-	how to verify it is working
	-	common troubleshooting steps
-	a short AI_USAGE.md describing:
	-	what AI tools you used, if any
	-	a few representative prompts
	-	how you verified the output before trusting it

Notes
-	You do not need to redesign the whole application.
-	Focus on practical, production-minded fixes.
-	Bonus points for improving operability, clarity, and safety.

## `docker-compose.yml`

```yaml
services:
  db:
    image: postgres:16-alpine
    container_name: student-access-db
    environment:
      POSTGRES_DB: kmk
      POSTGRES_USER: kmk_app
      POSTGRES_PASSWORD: kmk_password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./db/init.sql:/docker-entrypoint-initdb.d/init.sql:ro

  app:
    build:
      context: ./app
    container_name: student-access-app
    env_file:
      - .env
    depends_on:
      - db
    expose:
      - "8000"

  nginx:
    build:
      context: ./nginx
    container_name: student-access-nginx
    depends_on:
      - app
    ports:
      - "8080:80"

volumes:
  postgres_data:
```