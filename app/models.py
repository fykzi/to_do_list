from sqlalchemy import Column, Integer

from app.database import Base


class User(Base):
    """Пользователи"""

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
