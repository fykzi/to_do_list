from sqlalchemy.orm import Session
from models import User


async def create_and_get_user_id(db: Session):
    user = User()
    db.add(user)
    db.commit()
    db.refresh(user)
    return user.user_id
