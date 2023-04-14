from fastapi.testclient import TestClient
import pytest

from main import app


@pytest.fixture()
def client():
    with TestClient(app) as c:
        yield c


class TestEmployee():
    """Test Employee API"""
    def test_get_employees(self, client):
        """Test get employee"""
        response = client.get("/api/v1/employees")
        assert response.status_code == 200
        print(response.json())
