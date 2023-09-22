from sqlalchemy.orm import Session
from app.models import User


async def create_and_get_user_id(db: Session) -> int:
    """Создание пользователя и получения его `user_id`"""
    user = User()
    db.add(user)
    db.commit()
    db.refresh(user)
    return user.user_id
