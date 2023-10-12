from typing import Literal

from api.v1.users.services import _create_new_user
from database.session import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

user_router = APIRouter()


@user_router.post("/create-user")
async def create_user(
    db: AsyncSession = Depends(get_db),
) -> dict[Literal["user_id"], str]:
    return await _create_new_user(db)
