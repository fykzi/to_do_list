import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship

Base = declarative_base()


class User(Base):
    """DB ORM model with users"""

    __tablename__ = "users"

    user_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    task = relationship("Task")

    def __repr__(self):
        return f"ID: {self.user_id}"

    def __str__(self):
        return f"ID: {self.user_id}"

    def get_user_id(self) -> str:
        return str(self.user_id)


class Task(Base):
    """DB ORM model with tasks"""

    __tablename__ = "tasks"

    task_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(nullable=True)
    status: Mapped[bool] = mapped_column(default=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, nullable=True)
    completed_at = Column(DateTime, nullable=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.user_id"))

    def __repr__(self):
        return f"[ID: {self.task_id}, title: {self.title}]"

    def __str__(self):
        return f"[ID: {self.task_id}, title: {self.title}]"
