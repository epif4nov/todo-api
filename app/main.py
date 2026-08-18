from fastapi import FastAPI

from app.database import engine, Base
from app.routers import auth, tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo API")

app.include_router(auth.router)

app.include_router(tasks.router)