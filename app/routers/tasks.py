from fastapi import APIRouter, Depends, HTTPException, status
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

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Удаляет задачу пользователя по id"""
    task = db.query(Task).filter(Task.id == task_id).first()

    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Задача не найдена")

    if task.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Нет доступа к этой задаче")

    db.delete(task)
    db.commit()

    return {"detail": "Задача удалена"}

@router.patch("/{task_id}", response_model=TaskOut)
def toggle_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Переключает статус выполнения задачи"""
    task = db.query(Task).filter(Task.id == task_id).first()

    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Задача не найдена")

    if task.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Нет доступа к этой задаче")

    task.is_done = not task.is_done

    db.add(task)
    db.commit()
    db.refresh(task)

    return task