from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import User
from app.security import decode_access_token
from app.services.users import get_user_by_email


def get_db():
    """Создаёт сессию БД для одного запроса и закрывает её после"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    """Проверяет токен и возвращает текущего авторизованного пользователя"""
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Не удалось подтвердить учётные данные",
                            headers={"WWW-Authenticate": "Bearer"})

    email = payload.get("sub")
    if email is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Не удалось подтвердить учётные данные",
                            headers={"WWW-Authenticate": "Bearer"})


    user = get_user_by_email(
        db,
        email=email
    )

    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Не удалось подтвердить учётные данные",
                            headers={"WWW-Authenticate": "Bearer"})

    return user