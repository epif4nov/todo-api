from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models import Task, User
from app.schemas import TaskCreate


def create_task(
    db: Session,
    task_data: TaskCreate,
    current_user: User
):
    task = Task(
        title=task_data.title,
        owner_id=current_user.id
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


def get_user_tasks(
    db: Session,
    current_user: User
):
    tasks = (
        db.query(Task)
        .filter(Task.owner_id == current_user.id)
        .all()
    )

    return tasks


def delete_task(
    db: Session,
    task_id: int,
    current_user: User
):
    task = (
        db.query(Task)
        .filter(Task.id == task_id)
        .first()
    )

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Задача не найдена"
        )

    if task.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Нет доступа к этой задаче"
        )

    db.delete(task)
    db.commit()

    return {
        "detail": "Задача удалена"
    }


def toggle_task(
    db: Session,
    task_id: int,
    current_user: User
):
    task = (
        db.query(Task)
        .filter(Task.id == task_id)
        .first()
    )

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Задача не найдена"
        )

    if task.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Нет доступа к этой задаче"
        )

    task.is_done = not task.is_done

    db.add(task)
    db.commit()
    db.refresh(task)

    return task