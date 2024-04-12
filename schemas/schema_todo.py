from pydantic import BaseModel, ConfigDict


class TodoBase(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False


class TodoCreate(TodoBase):
    user_id: int | None = None


class Todo(TodoBase):
    id: int
    user_id: int

    class Config:
        model_config = ConfigDict(from_attributes=True)

