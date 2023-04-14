""" Celery app """
from celery import Celery


class CeleryWorker(Celery):
    """Celery worker."""
    def __init__(self, broker_url, result_backend, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conf.broker_url = broker_url
        self.conf.result_backend = result_backend

    def task(self, *args, **kwargs):
        """Create a task."""
        def wrapper(func):
            return super().task(*args, **kwargs)(func)
        return wrapper
