from datetime import datetime

from sqlalchemy import and_, delete, desc, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.tasks.shemas import Task as TaskShema
from database.models import Task, User


class BaseDal:
    """Base Data Access Layer with base methods"""

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session


class UserDAL(BaseDal):
    """Data Access Layer for operating user info"""

    async def create_user(self) -> User:
        new_user = User()
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user


class TaskDal(BaseDal):
    """Data Access Layer for operating task info"""

    async def create_task(self, task_info: TaskShema, user_id: str) -> None:
        new_task = Task(**task_info.dict())
        time_now = datetime.utcnow()
        new_task.created_at = time_now
        new_task.user_id = user_id
        self.db_session.add(new_task)
        await self.db_session.flush()

    async def get_tasks(self, user_id: str) -> list[Task]:
        query = (
            select(Task)
            .filter(Task.user_id == user_id)
            .order_by(Task.status)
            .order_by(desc(Task.completed_at))
            .order_by(desc(Task.created_at))
        )
        res = await self.db_session.execute(query)
        tasks = res.all()
        return tasks

    async def delete_task(self, user_id: str, task_id: int) -> None:
        query = delete(Task).where(
            and_(Task.user_id == user_id, Task.task_id == task_id)
        )
        await self.db_session.execute(query)

    async def update_task(self, user_id: str, task_id: int, task_info: dict) -> Task:
        time_now = datetime.utcnow()
        task_info["updated_at"] = time_now
        query = (
            update(Task)
            .where(and_(Task.user_id == user_id, Task.task_id == task_id))
            .values(**task_info)
        )
        await self.db_session.execute(query)
        return await self.get_only_one_task(user_id, task_id)

    async def get_only_one_task(self, user_id: str, task_id: int) -> Task:
        query = select(Task).where(
            and_(Task.user_id == user_id, Task.task_id == task_id)
        )
        res = await self.db_session.execute(query)
        task = res.fetchone()
        return task.Task

    async def complete_task(self, user_id: str, task_id: int) -> None:
        time_now = datetime.utcnow()
        query = (
            update(Task)
            .where(and_(Task.user_id == user_id, Task.task_id == task_id))
            .values(status=True, completed_at=time_now)
        )
        await self.db_session.execute(query)
