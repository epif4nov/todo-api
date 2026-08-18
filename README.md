# Todo API

REST API для трекера задач с регистрацией и JWT-авторизацией на FastAPI.

## Возможности

- Регистрация и вход пользователей с хэшированием паролей (bcrypt)
- JWT-авторизация для защищённых эндпоинтов
- CRUD задач: создание, просмотр, изменение статуса, удаление
- Каждый пользователь видит и управляет только своими задачами
- Автоматическая документация API (Swagger UI)
- Тесты на pytest с изолированной тестовой базой данных

## Технологии

- Python 3.12
- FastAPI
- SQLAlchemy (ORM)
- SQLite
- Pydantic (валидация данных)
- JWT (python-jose) для авторизации
- bcrypt (passlib) для хэширования паролей
- pytest для тестирования

## Установка

```bash
git clone https://github.com/epif4nov/todo-api.git
cd todo-api
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Запуск

```bash
uvicorn app.main:app --reload
```

После запуска документация доступна по адресу `http://127.0.0.1:8000/docs`

## Тесты

```bash
pytest tests/ -v
```

## Основные эндпоинты

| Метод | Путь | Описание |
|---|---|---|
| POST | `/auth/register` | Регистрация нового пользователя |
| POST | `/auth/login` | Вход, получение JWT-токена |
| POST | `/tasks/` | Создание задачи (требует авторизации) |
| GET | `/tasks/` | Список своих задач (требует авторизации) |
| PATCH | `/tasks/{task_id}` | Переключить статус выполнения задачи |
| DELETE | `/tasks/{task_id}` | Удалить задачу |

## Структура проекта

```
todo-api/
├── app/
│   ├── main.py            # точка входа, создание FastAPI-приложения
│   ├── database.py         # подключение к SQLite, сессия SQLAlchemy
│   ├── models.py            # ORM-модели: User, Task
│   ├── schemas.py            # Pydantic-схемы валидации
│   ├── security.py           # хэширование паролей, JWT
│   ├── dependencies.py       # get_db, get_current_user
│   └── routers/
│       ├── auth.py            # регистрация и вход
│       └── tasks.py           # CRUD задач
├── tests/
│   ├── conftest.py            # тестовая база данных и fixtures
│   └── test_auth.py           # тесты регистрации и входа
├── main.py
├── requirements.txt
└── README.md
```