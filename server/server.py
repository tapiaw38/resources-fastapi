from fastapi import FastAPI
from abc import ABC, abstractmethod
from database.database import DatabaseFactory
from repository.repository import set_repository
from celery_worker import CeleryWorker


class Config:
    """Base class for configuration."""
    def __init__(
        self,
        host: str,
        port: str,
        database_type: str,
        database_url: str,
        jwt_secret: str,
        celery_broker_url: str,
        celery_result_backend: str,
    ):
        self.host = host
        self.port = port
        self.database_type = database_type
        self.database_url = database_url
        self.jwt_secret = jwt_secret
        self.celery_broker_url = celery_broker_url
        self.celery_result_backend = celery_result_backend


class Server(ABC):
    """Base class for servers."""

    @abstractmethod
    def get_config(self):
        pass

    @abstractmethod
    def celery_worker(self):
        pass

    @abstractmethod
    def start(self):
        pass


class Broker(Server):
    """Base class for brokers."""

    def __init__(self, config: Config):
        self.config = config

    def get_config(self):
        """Get the configuration."""
        return self.config

    @property
    def celery_worker(self):
        """Create celery worker."""
        return CeleryWorker(
            broker_url=self.get_config().celery_broker_url,
            result_backend=self.get_config().celery_result_backend,
        )

    def start(self, binder_router, app: FastAPI):
        """Start the broker."""

        if self.get_config().database_url is None:
            raise ValueError("Database URL is not set.")

        if self.get_config().jwt_secret is None:
            raise ValueError("JWT secret is not set.")

        db = DatabaseFactory.create_database(
            self.get_config().database_url,
            self.get_config().database_type
        )

        set_repository(db)

        app.include_router(
            binder_router(broker=self),
            prefix="/api/v1",
        )
