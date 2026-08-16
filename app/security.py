from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    '''Хэширует пароль перед сохранением в базу данных'''
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    '''Проверяет, соответствует ли обычный пароль сохранённому хэшу'''
    return pwd_context.verify(plain_password, hashed_password)

