from pydantic import BaseModel


class Task(BaseModel):
    title: str
    description: str


class ShowTask(BaseModel):
    task_id: int
    title: str
    description: str
    status: bool


class UpdateTask(BaseModel):
    title: str = None
    description: str = None
