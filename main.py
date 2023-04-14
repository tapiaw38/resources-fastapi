from fastapi import FastAPI
from server.server import Config, Broker
from routers.routers import binder_router

from dotenv import load_dotenv
import os


app = FastAPI()
app.title = "Employee API"
app.description = "API for employee management"
app.version = "1.0.0"

load_dotenv()
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DATABASE_TYPE = os.getenv("DATABASE_TYPE")
DATABASE_URL = os.getenv("DATABASE_URL")
JWT_SECRET = os.getenv("JWT_SECRET")
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")

config = Config(
    host=HOST,
    port=PORT,
    database_type=DATABASE_TYPE,
    database_url=DATABASE_URL,
    jwt_secret=JWT_SECRET,
    celery_broker_url=CELERY_BROKER_URL,
    celery_result_backend=CELERY_RESULT_BACKEND,
)
broker = Broker(config=config)
broker.start(binder_router, app)
