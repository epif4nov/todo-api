from fastapi import FastAPI

from app.routers import auth, tasks


app = FastAPI(
    title="Todo API"
)

app.include_router(auth.router)

app.include_router(tasks.router)