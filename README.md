# Todo API

REST API для личных задач: регистрация, JWT-аутентификация и доступ только к своим данным.

**Python · FastAPI · SQLAlchemy · Alembic · SQLite / PostgreSQL**

## Что реализовано

- Регистрация с bcrypt-хэшированием; вход через OAuth2 password form и JWT.
- Создание и список задач, переключение статуса, удаление.
- Проверка владельца при изменении и удалении задачи.
- Миграция схемы Alembic, Docker Compose с PostgreSQL 16.
- Тесты регистрации, входа, CRUD, изоляции пользователей и ограничения пароля в UTF-8 байтах.

## Быстрый старт

Python 3.12+, команды из корня репозитория:

```sh
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
cp .env.example .env
```

В `.env` задайте `DATABASE_URL=sqlite:///./todo.db`. Создайте собственный `SECRET_KEY` командой `python -c "import secrets; print(secrets.token_urlsafe(32))"` и сохраните его в `.env`. Это локальная настройка; не добавляйте `.env` в Git.

```sh
alembic upgrade head
uvicorn app.main:app --reload
```

Swagger UI: `http://127.0.0.1:8000/docs`. Приложение не создаёт таблицы автоматически: миграция обязательна.

## Проверка

```sh
python -m pytest -q
```

Тесты сами задают конфигурацию до импорта приложения и используют отдельную SQLite in-memory базу. Рабочая база и пользовательский `.env` для них не нужны. PostgreSQL и сборка Docker проверяются отдельно, эти тесты их не заменяют.

## Docker / PostgreSQL

```sh
docker compose up -d postgres
# Дождитесь healthy-состояния PostgreSQL:
docker compose ps
docker compose run --rm api alembic upgrade head
docker compose up -d api
```

API доступен на порту `8001`, PostgreSQL — `5433`. `.env.docker` и учётные данные Compose предназначены для локальной разработки; перед внешним развёртыванием замените их. Удаление тома удаляет данные.

## Контракт API

| Метод | Путь | Действие |
| --- | --- | --- |
| POST | `/auth/register` | JSON: email, password |
| POST | `/auth/login` | Form: username=email, password |
| GET / POST | `/tasks/` | Список / создание задачи с Bearer-токеном |
| PATCH | `/tasks/{id}` | Переключение is_done |
| DELETE | `/tasks/{id}` | Удаление своей задачи |

Архитектура: `routers → dependencies / security → SQLAlchemy models → database`. Конфигурация — `app/config.py`, схема — `app/schemas.py`, миграции — `alembic/`, проверки — `tests/`.

## Границы проекта

Это учебное API. Пока нет пагинации, refresh-токенов, rate limiting и отдельного PostgreSQL integration suite. Подробности — [ROADMAP.md](ROADMAP.md).
