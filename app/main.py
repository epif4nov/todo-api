from fastapi import FastAPI

from app.routers import auth, tasks


app = FastAPI(
    title="Todo API",
    version="1.0.0"
)

app.include_router(
    auth.router,
    prefix="/api/v1"
)

app.include_router(
    tasks.router,
    prefix="/api/v1"
)