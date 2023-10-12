from typing import List, Literal

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.tasks.services import (
    _complete_task,
    _create_new_task,
    _delete_task,
    _get_tasks,
    _update_task,
)
from api.v1.tasks.shemas import ShowTask, Task, UpdateTask
from database.session import get_db

task_router = APIRouter()


@task_router.post("/create-task")
async def create_task(
    task_info: Task, user_id: str, db: AsyncSession = Depends(get_db)
) -> dict[Literal["message"], Literal["success"] | Literal["unsuccess"]]:
    return await _create_new_task(db, task_info, user_id)


@task_router.get("/get-tasks")
async def get_tasks(user_id: str, db: AsyncSession = Depends(get_db)) -> List[ShowTask]:
    res = await _get_tasks(db, user_id)
    if not res:
        raise HTTPException(status_code=400, detail="Create first task")
    return res


@task_router.delete("/delete-task")
async def delete_task(
    user_id: str, task_id: int, db: AsyncSession = Depends(get_db)
) -> dict[Literal["message"], Literal["success"] | Literal["unsuccess"]]:
    return await _delete_task(db, user_id, task_id)


@task_router.put("/update-task")
async def update_task(
    user_id: str,
    task_id: int,
    task_info: UpdateTask,
    db: AsyncSession = Depends(get_db),
) -> ShowTask | dict[Literal["message"], Literal["unsuccess"]]:
    return await _update_task(db, user_id, task_id, task_info)


@task_router.patch("/complete-task")
async def complete_task(
    task_id: int, user_id: str, db: AsyncSession = Depends(get_db)
) -> dict[Literal["message"], Literal["success"] | Literal["unsuccess"]]:
    return await _complete_task(db, user_id, task_id)
