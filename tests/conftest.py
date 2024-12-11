from contextlib import contextmanager
from datetime import datetime
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session
from projeto_fast.main import app
from projeto_fast.models import table_registry


@pytest.fixture()
def client():
    return TestClient(app)


@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
    table_registry.metadata.create_all(engine)

    connection = engine.connect()
    transaction = connection.begin()

    session = Session(bind=connection)
    yield session

    session.close()
    transaction.rollback()
    connection.close()
    table_registry.metadata.drop_all(engine)


@contextmanager
def _mock_db_time(*, model, time=datetime(2024, 1, 1)):
    def fake_time_handler(mapper, connection, target):
        for field in ("created_at", "updated_at"):
            if hasattr(target, field):
                setattr(target, field, time)

    event.listen(model, "before_insert", fake_time_handler)
    try:
        yield time
    finally:
        event.remove(model, "before_insert", fake_time_handler)


@pytest.fixture
def mock_db_time():
    return _mock_db_time
