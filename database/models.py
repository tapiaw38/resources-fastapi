from sqlalchemy import (
    Column, Integer, String,
    Numeric, Date, ForeignKey, TIMESTAMP
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class EmployeeType(Base):
    __tablename__ = 'employee_type'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), unique=True, index=True, nullable=False)
    description = Column(String(150))
    created_at = Column(TIMESTAMP, server_default='now()')
    updated_at = Column(TIMESTAMP, server_default='now()')


class Workplace(Base):
    __tablename__ = 'workplace'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    code = Column(String(150), unique=True, nullable=False)
    address = Column(String(150))
    created_at = Column(TIMESTAMP, server_default='now()')
    updated_at = Column(TIMESTAMP, server_default='now()')


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, index=True)
    file_code = Column(String(150), unique=True)
    agent_number = Column(String(150), unique=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), server_default='')
    document_number = Column(String(150), unique=True)
    birth_date = Column(Date)
    date_admission = Column(Date)
    phone = Column(String(150), server_default='')
    address = Column(String(150), server_default='')
    picture = Column(String(256), server_default='')
    salary = Column(Numeric(10, 2), server_default='0')
    category = Column(Integer, server_default='10')
    status = Column(Integer, server_default='1')
    work_number = Column(String(150), server_default='')
    employee_type = Column(
        Integer,
        ForeignKey('employee_type.id', ondelete='CASCADE')
    )
    workplace = Column(Integer, ForeignKey('workplace.id', ondelete='CASCADE'))
    created_at = Column(TIMESTAMP, server_default='now()')
    updated_at = Column(TIMESTAMP, server_default='now()')

    etype = relationship("EmployeeType", backref="employees")
    wplace = relationship("Workplace", backref="employees")


class Card(Base):
    __tablename__ = 'card'

    id = Column(Integer, primary_key=True, index=True)
    width = Column(Numeric(10, 2), nullable=False)
    height = Column(Numeric(10, 2), nullable=False)
    color = Column(String(150))
    created_at = Column(TIMESTAMP, server_default='now()')
    updated_at = Column(TIMESTAMP, server_default='now()')
