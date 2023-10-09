from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    task = relationship("Task")

    def __repr__(self):
        return f"ID: {self.user_id}"

    def __str__(self):
        return f"ID: {self.user_id}"


class Task(Base):
    __tablename__ = "tasks"

    task_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(nullable=True)
    status: Mapped[bool] = mapped_column(default=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, nullable=True)
    completed_at = Column(DateTime, nullable=True)
    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.user_id"), default="ade84cef-fd20-49dd-89a8-a222765bad60"
    )

    def __repr__(self):
        return f"[ID: {self.task_id}, title: {self.title}]"

    def __str__(self):
        return f"[ID: {self.task_id}, title: {self.title}]"
