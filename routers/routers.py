from fastapi import APIRouter

from routers.employee import employee_routers


def binder_router(broker):
    """Bind the routers to the app."""

    app = APIRouter()

    app.include_router(
        employee_routers(broker),
        prefix="/employees",
        tags=["employees"]
    )

    return app
