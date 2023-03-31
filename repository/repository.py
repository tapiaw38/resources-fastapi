from database.models import Employee
from abc import ABC, abstractmethod
from typing import List, Optional


def set_repository(impl) -> None:
    """Set the implementation."""
    global implementation
    implementation = impl


class BaseRepository(ABC):
    """ Base class for employee repositories. """

    @abstractmethod
    def create_employee(self, employee: Employee) -> Employee:
        pass

    @abstractmethod
    def get_employee_by_id(self, employee_id: int) -> Optional[Employee]:
        pass

    @abstractmethod
    def get_employee_by_type(self, employee_type: int) -> List[Employee]:
        pass

    @abstractmethod
    def get_all_employees(self) -> List[Employee]:
        pass

    @abstractmethod
    def update_employee(
        self,
        employee_id: int,
        employee: Employee,
    ) -> Optional[Employee]:
        pass

    @abstractmethod
    def delete_employee(self, employee_id: int) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass


class Repository(BaseRepository):
    """ Repository is a facade for the implementation. """

    def create_employee(self, employee: Employee) -> Employee:
        return implementation.create_employee(employee)

    def get_employee_by_id(self, employee_id: int) -> Optional[Employee]:
        return implementation.get_employee_by_id(employee_id)

    def get_employee_by_type(self, employee_type: int) -> List[Employee]:
        return implementation.get_employee_by_type(employee_type)

    def get_all_employees(self) -> List[Employee]:
        return implementation.get_all_employees()

    def update_employee(
        self,
        employee_id: int,
        employee: Employee,
    ) -> Optional[Employee]:
        return implementation.update_employee(employee_id, employee)

    def delete_employee(self, employee_id: int) -> None:
        return implementation.delete_employee(employee_id)

    def close(self) -> None:
        return implementation.close()
