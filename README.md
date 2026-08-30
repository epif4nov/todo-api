# Todo API

REST API for managing personal tasks, built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **JWT authentication**.

The project demonstrates backend development with authentication, database migrations, automated tests, and Docker-based infrastructure.

## Features

- User registration
- JWT authentication
- Password hashing
- Protected endpoints
- Create tasks
- Get personal tasks
- Update task status
- Delete tasks
- Task ownership protection
- PostgreSQL database
- Alembic database migrations
- Automated tests with Pytest
- Docker and Docker Compose
- PostgreSQL healthcheck
- Automatic migrations before API startup

## Tech Stack

- Python
- FastAPI
- PostgreSQL 16
- SQLAlchemy
- Alembic
- Pydantic
- JWT
- Pytest
- Docker
- Docker Compose

## Project Structure

```text
todo-api/
├── app/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   ├── config.py
│   ├── database.py
│   └── main.py
│
├── alembic/
│   └── versions/
│
├── tests/
│
├── .env.docker.example
├── .gitignore
├── alembic.ini
├── docker-compose.yml
├── Dockerfile
├── pytest.ini
├── requirements.txt
├── ROADMAP.md
└── README.md
```

## Quick Start with Docker

### 1. Clone the repository

```bash
git clone https://github.com/epif4nov/todo-api.git
cd todo-api
```

### 2. Create the Docker environment file

Windows PowerShell:

```powershell
Copy-Item .env.docker.example .env.docker
```

Linux / macOS:

```bash
cp .env.docker.example .env.docker
```

Example configuration:

```env
DATABASE_URL=postgresql://todo:todo@postgres:5432/todo
SECRET_KEY=change-me
ACCESS_TOKEN_EXPIRE_MINUTES=30
JWT_ALGORITHM=HS256
```

For real deployments, replace the example secret and database credentials with secure values.

### 3. Start the application

```bash
docker compose up -d --build
```

Docker Compose starts the application in the following order:

```text
PostgreSQL
    ↓
Healthcheck
    ↓
Alembic migrations
    ↓
FastAPI
```

The PostgreSQL healthcheck ensures that the database is ready before Alembic attempts to connect.

The `migrate` service then runs:

```bash
alembic upgrade head
```

The API starts only after the migrations complete successfully.

### 4. Check container status

```bash
docker compose ps -a
```

A successful startup should look approximately like this:

```text
postgres   Up (healthy)
migrate    Exited (0)
api        Up
```

`migrate` exiting with code `0` is expected. It applies the migrations and then finishes its work.

## API Documentation

After the application starts, Swagger UI is available at:

```text
http://localhost:8001/docs
```

ReDoc is available at:

```text
http://localhost:8001/redoc
```

## Database

The project uses **PostgreSQL 16**.

Inside the Docker Compose network, the application connects to PostgreSQL using:

```text
postgres:5432
```

From the host machine, PostgreSQL is available at:

```text
localhost:5434
```

Database data is stored in a Docker volume and survives normal container restarts.

Stop the application:

```bash
docker compose down
```

Stop the application and delete the PostgreSQL volume:

```bash
docker compose down -v
```

> `docker compose down -v` permanently removes the database data stored in the Docker volume.

## Database Migrations

Database schema changes are managed with **Alembic**.

### Check the current migration

With Docker services running:

```bash
docker compose exec api alembic current
```

### Apply all migrations

```bash
alembic upgrade head
```

### Create a new migration

After changing SQLAlchemy models:

```bash
alembic revision --autogenerate -m "describe migration"
```

Review the generated migration and then apply it:

```bash
alembic upgrade head
```

## Tests

Run the complete test suite with:

```bash
pytest
```

For shorter output:

```bash
pytest -q
```

The current test suite covers authentication and task operations.

## Local Development

Docker is the recommended way to run the complete project, but the FastAPI application can also be started locally.

### 1. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Linux / macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start PostgreSQL

PostgreSQL can still run through Docker:

```bash
docker compose up -d postgres
```

When the Python application runs directly on the host machine, the database connection must use the exposed host port:

```env
DATABASE_URL=postgresql://todo:todo@localhost:5434/todo
```

Inside Docker, the connection uses:

```env
DATABASE_URL=postgresql://todo:todo@postgres:5432/todo
```

### 4. Apply migrations

```bash
alembic upgrade head
```

### 5. Start FastAPI

```bash
uvicorn app.main:app --reload
```

Swagger UI will then be available at the port configured for the local Uvicorn process.

## Environment Variables

| Variable | Description |
| --- | --- |
| `DATABASE_URL` | PostgreSQL connection URL |
| `SECRET_KEY` | Secret key used for JWT signing |
| `JWT_ALGORITHM` | JWT signing algorithm |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Access token lifetime in minutes |

Real environment files should not be committed to Git.

The repository contains:

```text
.env.docker.example
```

as a safe configuration template.

Create your own local:

```text
.env.docker
```

from that template before starting the project.

## Current Status

Implemented:

- FastAPI project structure
- SQLAlchemy models
- User registration
- Password hashing
- JWT authentication
- Protected routes
- Task CRUD operations
- Task ownership
- PostgreSQL integration
- Alembic migrations
- Environment-based configuration
- Automated tests
- Docker image
- Docker Compose
- PostgreSQL healthcheck
- Automatic database migrations before API startup

Further development plans are tracked in [`ROADMAP.md`](ROADMAP.md).