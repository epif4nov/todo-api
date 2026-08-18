from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db, get_current_user
from app.schemas import TaskCreate, TaskOut
from app.models import Task, User

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/", response_model=TaskOut)
def create_task(task_data: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Создаёт новую задачу для текущего пользователя"""
    task = Task(title=task_data.title,
                owner_id=current_user.id)

    db.add(task)
    db.commit()
    db.refresh(task)

    return task

@router.get("/", response_model=list[TaskOut])
def get_tasks(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    tasks = db.query(Task).filter(Task.owner_id == current_user.id).all()
    return tasks