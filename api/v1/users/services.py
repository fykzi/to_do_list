from typing import Literal

from sqlalchemy.ext.asyncio import AsyncSession
from database.dals import UserDAL


async def _create_new_user(db: AsyncSession) -> dict[Literal["user_id"], str]:
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            new_user = await user_dal.create_user()
            message = {"user_id": new_user.get_user_id()}
            return message
