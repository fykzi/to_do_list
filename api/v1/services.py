from sqlalchemy.ext.asyncio import AsyncSession
from api.v1.shemas import Task, ShowTask, UpdateTask
from database.dals import UserDAL, TaskDal
from fastapi import Response

from typing import List


async def _create_new_user(db: AsyncSession, response: Response) -> dict:
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            new_user = await user_dal.create_user()
            message = {"user_id": new_user.user_id}
            return message


async def _create_new_task(db: AsyncSession, task_info: Task, user_id: str) -> dict:
    async with db as session:
        async with session.begin():
            task_dal = TaskDal(session)
            try:
                await task_dal.create_task(task_info, user_id)
                message = {"message": "success"}
            except:
                message = {"message": "unsuccess"}
            return message


async def _get_tasks(db: AsyncSession, user_id: str) -> List[ShowTask]:
    async with db as session:
        async with session.begin():
            task_dal = TaskDal(session)
            tasks = await task_dal.get_tasks(user_id)
            if tasks:
                res = []
                for i in tasks:
                    task = i.Task
                    task_for_resp = ShowTask(
                        task_id=task.task_id,
                        title=task.title,
                        description=task.description,
                        status=task.status,
                    )
                    res.append(task_for_resp)
                return res


async def _delete_task(db: AsyncSession, user_id: str, task_id: int) -> dict:
    async with db as session:
        async with session.begin():
            task_dal = TaskDal(session)
            try:
                await task_dal.delete_task(user_id, task_id)
                message = {"message": "success"}
            except:
                message = {"message": "unsuccess"}
            return message


async def _update_task(
    db: AsyncSession, user_id: str, task_id: int, task_info: UpdateTask
) -> ShowTask | dict:
    async with db as session:
        async with session.begin():
            validate_task_info = {
                k: v for k, v in task_info.dict().items() if v is not None
            }

            task_dal = TaskDal(session)
            try:
                update_task = await task_dal.update_task(
                    user_id, task_id, validate_task_info
                )
                return ShowTask(
                    task_id=update_task.task_id,
                    title=update_task.title,
                    description=update_task.description,
                    status=update_task.status,
                )
            except:
                message = {"message": "unsuccess"}
                return message


async def _complete_task(db: AsyncSession, user_id: str, task_id: int) -> dict:
    async with db as session:
        async with session.begin():
            task_dal = TaskDal(db)
            try:
                await task_dal.complete_task(user_id, task_id)
                message = {"message": "success"}
            except:
                message = {"message:" "unsuccess"}
            return message
