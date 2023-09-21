from fastapi import Depends
from sqlalchemy.orm import Session
from services import create_and_get_user_id
from utils import get_db

from config import create_app


app = create_app()


@app.post("/get-user-id/")
async def get_user_id(db: Session = Depends(get_db)):
    """Сервис получения id для новых пользователей"""
    user_id = await create_and_get_user_id(db)
    return {"user_id": user_id}


@app.get("/get-tasks/")
async def root():
    pass
