from abc import ABC, abstractmethod
from database.database import DatabaseFactory
from repository.repository import set_repository


class Config:
    """Base class for configuration."""

    def __init__(
        self,
        host: str,
        port: str,
        database_type: str,
        database_url: str,
        jwt_secret: str,
    ):
        self.host = host
        self.port = port
        self.database_type = database_type
        self.database_url = database_url
        self.jwt_secret = jwt_secret


class Server(ABC):
    """Base class for servers."""

    @abstractmethod
    def get_config(self):
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

    def start(self, fast_app, binder_router):
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

        fast_app.include_router(
            binder_router(self.get_config()),
            prefix="/api/v1",
        )
