from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str

class TaskOut(BaseModel):
    id: int
    title: str
    is_done: bool
    owner_id: int

    class Config:
        from_attributes = True