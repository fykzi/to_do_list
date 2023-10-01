import os
from dotenv import load_dotenv


load_dotenv()


ALLOW_ORIGINS = ["http://localhost:5173/", "http://185.196.117.170:5200"]
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")
