from fastapi import APIRouter, Depends, Cookie, Response
from sqlalchemy.ext.asyncio import AsyncSession
from api.v1.shemas import Task, ShowTask, UpdateTask
from database.session import get_db
from fastapi.exceptions import HTTPException
from typing import List

from api.v1.services import (
    _create_new_user,
    _create_new_task,
    _get_tasks,
    _delete_task,
    _update_task,
    _complete_task,
)

user_router = APIRouter()


@user_router.post("/create-user")
async def create_user(db: AsyncSession = Depends(get_db)) -> dict:
    return await _create_new_user(db)


task_router = APIRouter()


@task_router.post("/create-task")
async def create_task(
    task_info: Task, user_id: str, db: AsyncSession = Depends(get_db)
) -> dict:
    return await _create_new_task(db, task_info, user_id)


@task_router.get("/get-tasks")
async def get_tasks(user_id: str, db: AsyncSession = Depends(get_db)) -> List[ShowTask]:
    res = await _get_tasks(db, user_id)
    if not res:
        raise HTTPException(status_code=400, detail="Не удалоcь получить ваши задачи")
    return res


@task_router.delete("/delete-task")
async def delete_task(
    user_id: str, task_id: int, db: AsyncSession = Depends(get_db)
) -> dict:
    return await _delete_task(db, user_id, task_id)


@task_router.put("/update-task")
async def update_task(
    user_id: str,
    task_id: int,
    task_info: UpdateTask,
    db: AsyncSession = Depends(get_db),
) -> ShowTask | dict:
    return await _update_task(db, user_id, task_id, task_info)


@task_router.patch("/complete-task")
async def complete_task(
    task_id: int, user_id: str, db: AsyncSession = Depends(get_db)
) -> dict:
    return await _complete_task(db, user_id, task_id)
