from app import models
from app.database import engine
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI


allow_origins = ["*"]


def create_app() -> FastAPI:
    """Создание приложения FastAPI"""
    app = FastAPI()

    app.add_middleware(CORSMiddleware, allow_origins=allow_origins)

    models.Base.metadata.create_all(bind=engine)

    return app
