from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from typing import Generator

from app import settings

engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URL, future=True, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_db() -> Generator:
    """Получение базы данных"""
    try:
        session: AsyncSession = async_session()
        yield session
    finally:
        await session.close()
