import pytest
from fastapi.testclient import TestClient
from projeto_fast.main import app


@pytest.fixture()
def client():
    return TestClient(app)
