# from fastapi import Depends, Response
# from sqlalchemy.orm import Session
# from app.services import create_and_get_user_id
# from app.utils import get_db

# import uvicorn

# from app.settings import create_app
# from .shemas import *


# app = create_app()


# @app.post("/get-user-id")
# async def get_user_id(db: Session = Depends(get_db)) -> dict:
#     """Сервис получения id для новых пользователей"""
#     user_id = AllUsers.last()
#     user = Users(user_id=user_id)
#     AllUsers.add_user(user)
#     return {"user_id": user_id}


# @app.post("/user/{user_id}/create-tasks")
# async def create_tasks(user_id: int, task: Tasks) -> dict:
#     task_id = AllTasks.last()
#     task.task_id = task_id
#     task.created_at = f"{datetime.now():%d.%m.%Y в %H:%M}"
#     AllTasks.add_task(task)
#     AllUserTasks.add_user_task(user_id=user_id, task_id=task_id)
#     return {"message": "success"}


# @app.get("/user/{user_id}/get-tasks")
# async def get_tasks(user_id: int) -> dict:
#     result = AllUserTasks.get_user_task(user_id)
#     if not result:
#         unsuccess_response = {"message": "task not found"}
#         return unsuccess_response
#     return {"tasks": result}


# @app.delete("/user/{user_id}/delete-task")
# async def delete_user_task(user_id: int, task_id: int) -> dict:
#     AllUserTasks.delete_user_task(user_id=user_id, task_id=task_id)
#     return {"message": "success"}


import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from app import settings
from api.v1.handlers import user_router, task_router
from pathlib import Path

app = FastAPI(title="To do list")

app.add_middleware(
    CORSMiddleware, allow_origins=settings.ALLOW_ORIGINS, allow_credentials=True
)


main_api_router = APIRouter()

app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(task_router, prefix="/task", tags=["task"])
