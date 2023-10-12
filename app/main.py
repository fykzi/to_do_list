from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.v1.tasks.handlers import task_router
from api.v1.users.handlers import user_router
from app import settings

app = FastAPI(title="To do list")

app.add_middleware(
    CORSMiddleware, allow_origins=settings.ALLOW_ORIGINS, allow_credentials=True
)


main_api_router = APIRouter()

app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(task_router, prefix="/task", tags=["task"])
