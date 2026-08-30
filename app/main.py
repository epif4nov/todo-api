from fastapi import FastAPI

from app.routers.auth import router as auth_router
from app.routers.health import router as health_router
from app.routers.tasks import router as tasks_router

app = FastAPI(
    title="Todo API"
)

app.include_router(health_router)
app.include_router(auth_router)
app.include_router(tasks_router)