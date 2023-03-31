from pydantic import BaseModel, Field


class Employee(BaseModel):
    """Employee model."""
    file_code: str = Field(default=None, max_length=50)
    agent_number: str = Field(default=None, max_length=50)
    first_name: str = Field(..., min_length=2, max_length=50)
    last_name: str = Field(default=None, max_length=50)
    document_number: str = Field(..., min_length=8, max_length=8)
    birth_date: str = Field(default=None, max_length=19)
    date_admission: str = Field(default=None, max_length=19)
    phone: str = Field(default=None, max_length=50)
    address: str = Field(default=None, max_length=150)
    picture: str = Field(default=None, max_length=256)
    salary: float = Field(default=None)
    category: int = Field(default=None, ge=1, le=30)
    status: int = Field(default=None, ge=1, le=10)
    work_number: str = Field(default=None, max_length=50)
    employee_type: int = Field(default=None, ge=1, le=1000)
    workplace: int = Field(default=None, ge=1, le=1000)

    class Config:
        schema_extra = {
            "example": {
                "file_code": "1231231231244124",
                "agent_number": "12333123231123",
                "first_name": "John",
                "last_name": "Doe",
                "document_number": "12345678",
                "birth_date": "2020-01-01",
                "date_admission": "2020-01-01",
                "phone": "",
                "address": "",
                "picture": "",
                "salary": 1000.00,
                "category": 1,
                "status": 1,
                "work_number": "123456789",
                "employee_type": 1,
                "workplace": 1,
            }
        }
