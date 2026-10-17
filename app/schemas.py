from pydantic import BaseModel, EmailStr, Field, field_validator, ConfigDict

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)

    @field_validator("password")
    @classmethod
    def password_fits_bcrypt(cls, value: str) -> str:
        if len(value.encode("utf-8")) > 72:
            raise ValueError("Password must fit within 72 UTF-8 bytes")
        return value

class UserOut(BaseModel):
    id: int
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)

class TaskCreate(BaseModel):
    title: str

class TaskOut(BaseModel):
    id: int
    title: str
    is_done: bool
    owner_id: int

    model_config = ConfigDict(from_attributes=True)
