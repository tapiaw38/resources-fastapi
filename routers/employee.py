from fastapi import APIRouter
from fastapi import Body, Path, Query

from typing import Optional, List
from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException
from starlette.status import (
    HTTP_200_OK, HTTP_201_CREATED,
    HTTP_404_NOT_FOUND
)
from fastapi.encoders import jsonable_encoder
from models.employee import Employee

from repository.repository import Repository

repository = Repository()


def employee_routers(config):
    """Bind the employee router to the app."""

    employee_router = APIRouter()

    @employee_router.get("", response_model=List[Employee])
    def get_employees() -> List[Employee]:
        """Get all employees."""
        employees = repository.get_all_employees()
        return JSONResponse(
            status_code=HTTP_200_OK,
            content=jsonable_encoder(employees)
        )

    @employee_router.get("/{employee_id}", response_model=Employee)
    def get_employee(employee_id: int = Path(..., ge=1)) -> Employee:
        """Get employee by id."""
        employee = repository.get_employee_by_id(employee_id)
        if employee is not None:
            return JSONResponse(
                status_code=HTTP_200_OK,
                content=jsonable_encoder(employee)
            )
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail="employee not found"
        )

    @employee_router.get("/", response_model=List[Employee])
    def get_employee_by_type(
        employee_type: int = Query(..., ge=1, le=10)
    ) -> List[Employee]:
        """Get employees by type."""
        employees = repository.get_employee_by_type(employee_type)
        return JSONResponse(
            status_code=HTTP_200_OK,
            content=jsonable_encoder(employees)
        )

    @employee_router.post("/", response_model=Employee)
    def create_employee(employee: Employee = Body(...)) -> Employee:
        """Create a new employee."""
        employee = repository.create_employee(employee)
        return JSONResponse(
            status_code=HTTP_201_CREATED,
            content=jsonable_encoder(employee)
        )

    @employee_router.put("/{employee_id}", response_model=Employee)
    def update_employee(
        employee_id: int,
        employee: Employee = Body(...),
    ) -> Optional[Employee]:
        """Update employee by id."""
        employee = repository.update_employee(employee_id, employee)
        if employee is not None:
            return JSONResponse(
                status_code=HTTP_200_OK,
                content=jsonable_encoder(employee)
            )
        raise HTTPException(
            status_code=404,
            detail="employee not found"
        )

    @employee_router.delete("/{employee_id}", response_model=Employee)
    def delete_employee(employee_id: int) -> Optional[Employee]:
        """Delete employee by id."""
        employee = repository.delete_employee(employee_id)
        if employee is not None:
            return JSONResponse(
                status_code=HTTP_200_OK,
                content=jsonable_encoder(employee)
            )
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail="employee not found"
        )

    return employee_router
