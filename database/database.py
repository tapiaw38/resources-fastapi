from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from database.models import Employee
from typing import List, Optional, Union
from datetime import datetime


class PostgresDatabase:
    """ Postgres database. """

    _instance = None

    def __new__(cls, db_url: str):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.engine = create_engine(db_url)
            cls._instance.session = sessionmaker(bind=cls._instance.engine)()
            cls._instance.base = declarative_base()
            cls._instance.create_tables()
        return cls._instance

    def get_session(self):
        return self._instance.session

    def get_base(self):
        return self._instance.base

    def get_engine(self):
        return self._instance.engine

    def create_tables(self):
        self.get_base().metadata.create_all(bind=self.get_engine())

    def create_employee(self, employee: Employee) -> Employee:
        """ Create a new employee."""
        new_employee = Employee(**employee.dict())
        self.get_session().add(new_employee)
        self.get_session().commit()
        self.get_session().refresh(new_employee)
        return new_employee

    def get_employee_by_id(self, employee_id: int) -> Optional[Employee]:
        """ Get employee by id."""
        return self.get_session().query(Employee).filter_by(
            id=employee_id).first()

    def get_employee_by_type(self, employee_type: int) -> List[Employee]:
        """ Get employee by type."""
        return self.get_session().query(Employee).filter_by(
                employee_type=employee_type
            ).all()

    def get_all_employees(self) -> List[Employee]:
        """ Get all employees."""
        return self.get_session().query(Employee).all()

    def update_employee(
        self,
        employee_id: int,
        employee: Employee,
    ) -> Optional[Employee]:
        """ Update employee."""
        update_employee = self.get_session().query(Employee).filter_by(
            id=employee_id).first()

        if update_employee:
            update_employee.first_name = employee.first_name
            update_employee.last_name = employee.last_name
            update_employee.document_number = employee.document_number
            update_employee.birth_date = employee.birth_date
            update_employee.date_admission = employee.date_admission
            update_employee.phone = employee.phone
            update_employee.address = employee.address
            update_employee.picture = employee.picture
            update_employee.salary = employee.salary
            update_employee.category = employee.category
            update_employee.status = employee.status
            update_employee.work_number = employee.work_number
            update_employee.employee_type = employee.employee_type
            update_employee.workplace = employee.workplace
            update_employee.updated_at = datetime.now()
            self.get_session().commit()
            self.get_session().refresh(update_employee)
            return update_employee
        return None

    def delete_employee(self, employee_id: int) -> Optional[Employee]:
        """ Delete employee."""
        delete_employee = self.get_session().query(
            Employee).filter_by(id=employee_id).first()
        if delete_employee:
            self.get_session().delete(delete_employee)
            self.get_session().commit()
            return delete_employee
        return None

    def close(self) -> None:
        """ Close session."""
        self.get_session().close()


class MongoDatabase:
    """ Mongo database. """
    pass


class DatabaseFactory:
    """ Factory for database. """
    @staticmethod
    def create_database(
        db_url: str, db_type: str
    ) -> Optional[Union[PostgresDatabase, MongoDatabase]]:
        if db_type == "postgres":
            return PostgresDatabase(db_url)
        elif db_type == "mongo":
            return MongoDatabase(db_url)
        else:
            return Exception("Database type not supported")
