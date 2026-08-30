# Todo API — Roadmap

This roadmap tracks the development of the Todo API from a basic FastAPI application toward a more production-ready backend project.

## ✅ Core API

- [x] FastAPI application setup
- [x] Project structure
- [x] SQLAlchemy integration
- [x] User model
- [x] Task model
- [x] User registration
- [x] Password hashing
- [x] JWT authentication
- [x] Protected routes
- [x] Task creation
- [x] Get user tasks
- [x] Update task status
- [x] Delete tasks
- [x] Task ownership protection

## ✅ Database

- [x] PostgreSQL instead of SQLite
- [x] SQLAlchemy database configuration
- [x] Alembic migrations
- [x] Initial database migration
- [x] Task ownership migration
- [x] Environment-based database configuration
- [x] Persistent PostgreSQL Docker volume

## ✅ Testing

- [x] Pytest setup
- [x] Authentication tests
- [x] Task tests
- [x] Test database setup
- [x] Authentication service tests
- [x] Task ownership tests

## ✅ Docker

- [x] Dockerfile
- [x] Docker Compose
- [x] PostgreSQL container
- [x] FastAPI container
- [x] Docker environment configuration
- [x] PostgreSQL healthcheck
- [x] Dedicated migration service
- [x] Automatic Alembic migrations before API startup
- [x] Persistent database storage
- [x] `.env.docker.example`

## ✅ Documentation

- [x] README
- [x] Docker setup documentation
- [x] PostgreSQL documentation
- [x] Alembic migration documentation
- [x] Environment variable documentation
- [x] Local development instructions
- [x] Testing instructions

---

# Next Steps

## 🔄 CI — GitHub Actions

- [ ] Add GitHub Actions workflow
- [ ] Run tests automatically on every push
- [ ] Run tests automatically on pull requests
- [ ] Install dependencies in CI
- [ ] Add PostgreSQL service for integration tests
- [ ] Prevent merging when tests fail

Goal:

```text
git push
    ↓
GitHub Actions
    ↓
install dependencies
    ↓
start test environment
    ↓
run pytest
    ↓
pass / fail
```

This will ensure that changes are automatically verified before they are merged.

---

## 🧹 Code Quality

- [ ] Add Ruff
- [ ] Add code formatting checks
- [ ] Add linting to GitHub Actions
- [ ] Fix current deprecation warnings
- [ ] Migrate Pydantic configuration to `ConfigDict`
- [ ] Review dependency versions
- [ ] Improve type hints

Possible CI pipeline:

```text
push / pull request
        ↓
Ruff
        ↓
Pytest
        ↓
Build Docker image
```

---

## 🔐 Authentication Improvements

- [ ] Add refresh tokens
- [ ] Add token refresh endpoint
- [ ] Add logout / token revocation strategy
- [ ] Add user profile endpoint
- [ ] Add password change endpoint
- [ ] Improve authentication error responses

Possible future authentication flow:

```text
login
  ↓
access token
+
refresh token

access token expires
  ↓
refresh token
  ↓
new access token
```

---

## 👤 User Management

- [ ] Get current user profile
- [ ] Update user profile
- [ ] Change password
- [ ] Delete user account
- [ ] Prevent duplicate usernames / emails with clear API errors

---

## 📝 Task Improvements

- [ ] Add task title validation
- [ ] Add task description
- [ ] Add task creation timestamp
- [ ] Add task update timestamp
- [ ] Add due date
- [ ] Add priority
- [ ] Add task categories
- [ ] Add task filtering
- [ ] Add task sorting
- [ ] Add pagination
- [ ] Add search

Example:

```text
GET /tasks
    ?completed=false
    &priority=high
    &limit=20
    &offset=0
```

---

## ⚠️ Error Handling

- [ ] Create centralized exception handlers
- [ ] Standardize API error responses
- [ ] Improve validation errors
- [ ] Add custom application exceptions
- [ ] Avoid exposing internal errors to clients

Target error format:

```json
{
  "detail": "Task not found"
}
```

Later this may evolve into:

```json
{
  "error": {
    "code": "TASK_NOT_FOUND",
    "message": "Task not found"
  }
}
```

---

## 📊 Logging

- [ ] Add application logging
- [ ] Log startup and shutdown events
- [ ] Log authentication failures
- [ ] Log unexpected server errors
- [ ] Configure structured logging
- [ ] Add request IDs / correlation IDs

---

## 🩺 Application Health

- [ ] Add `/health` endpoint
- [ ] Check application health
- [ ] Check database connectivity
- [ ] Add FastAPI healthcheck to Docker Compose

Example:

```text
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

---

## 🐳 Docker Improvements

- [ ] Optimize Docker image size
- [ ] Use a multi-stage Docker build
- [ ] Run application as a non-root user
- [ ] Add FastAPI container healthcheck
- [ ] Review Docker security settings
- [ ] Add production-specific Docker configuration

---

## 🧪 Testing Improvements

- [ ] Increase authentication test coverage
- [ ] Increase task test coverage
- [ ] Add permission tests
- [ ] Add validation tests
- [ ] Add migration tests
- [ ] Add database integration tests
- [ ] Add API error tests
- [ ] Add health endpoint tests
- [ ] Generate test coverage report

Possible future command:

```bash
pytest --cov=app
```

---

## 🚦 API Improvements

- [ ] Add API versioning

Example:

```text
/api/v1/auth
/api/v1/tasks
```

- [ ] Add pagination metadata
- [ ] Standardize API responses
- [ ] Improve OpenAPI descriptions
- [ ] Add endpoint tags and examples
- [ ] Improve Swagger documentation

---

## 🛡️ Security

- [ ] Review JWT security
- [ ] Improve secret management
- [ ] Add CORS configuration
- [ ] Add rate limiting
- [ ] Add secure production settings
- [ ] Validate environment configuration on startup
- [ ] Review Docker security
- [ ] Add security-related HTTP headers where applicable

---

## 🚀 Deployment

- [ ] Create production configuration
- [ ] Build production Docker image
- [ ] Add Docker image build to CI
- [ ] Deploy API to a cloud/VPS environment
- [ ] Deploy PostgreSQL database
- [ ] Configure HTTPS
- [ ] Configure domain
- [ ] Configure environment secrets
- [ ] Run Alembic migrations during deployment

Target architecture:

```text
Internet
   ↓
HTTPS
   ↓
Reverse Proxy
   ↓
FastAPI
   ↓
PostgreSQL
```

---

## 📈 Future / Advanced

- [ ] Redis integration
- [ ] Background jobs
- [ ] Email notifications
- [ ] Task reminders
- [ ] Metrics
- [ ] Monitoring
- [ ] OpenTelemetry
- [ ] Automated database backups
- [ ] Production observability

---

# Current Priority

The next major milestone is:

## GitHub Actions CI

The goal is to automatically verify every change before it is merged.

Planned order:

```text
1. GitHub Actions
2. Ruff / code quality
3. Fix deprecation warnings
4. Improve tests
5. Add health endpoint
6. Improve task functionality
7. Authentication improvements
8. Production Docker improvements
9. Deployment
```

The project currently has a working foundation:

```text
FastAPI
   +
PostgreSQL
   +
SQLAlchemy
   +
Alembic
   +
JWT
   +
Pytest
   +
Docker
```

The next phase focuses on automation, code quality, reliability, and production readiness.