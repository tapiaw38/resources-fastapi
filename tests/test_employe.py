from fastapi.testclient import TestClient
import pytest

from main import app

client = TestClient(app)


class TestEmployee():

    def test_employee(self, client: TestClient):
        response = client.get("/api/v1/employees")
        assert response.status_code == 200
