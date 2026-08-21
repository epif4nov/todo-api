from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError

from app.config import settings

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

ALGORITHM = "HS256"

def hash_password(password: str) -> str:
    """Хэширует пароль перед сохранением в базу данных"""
    return pwd_context.hash(password)

def verify_password(
        plain_password: str,
        hashed_password: str
) -> bool:
    """Проверяет, соответствует ли обычный пароль сохранённому хэшу"""
    return pwd_context.verify(
        plain_password,
        hashed_password)


def create_access_token(data: dict) -> str:
    """Создаёт JWT-токен с данными пользователя и сроком действия"""
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=ALGORITHM
    )

def decode_access_token(token: str) -> dict | None:
    """Декодирует и проверяет JWT-токен. Возвращает payload или None при ошибке"""

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:
        return None