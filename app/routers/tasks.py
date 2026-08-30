from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_current_user, get_db
from app.models import User
from app.schemas import TaskCreate, TaskOut
from app.services.tasks import create_task, delete_task, get_user_tasks, toggle_task

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)


@router.post("/", response_model=TaskOut)
def create(
    task_data: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_task(
        db,
        task_data,
        current_user
    )


@router.get("/", response_model=list[TaskOut])
def get_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_user_tasks(
        db,
        current_user
    )


@router.delete("/{task_id}")
def delete(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return delete_task(
        db,
        task_id,
        current_user
    )


@router.patch("/{task_id}", response_model=TaskOut)
def toggle(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return toggle_task(
        db,
        task_id,
        current_user
    )