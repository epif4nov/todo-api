from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True

class TaskCreate(BaseModel):
    title: str

class TaskOut(BaseModel):
    id: int
    title: str
    is_done: bool
    owner_id: int

    class Config:
        from_attributes = True