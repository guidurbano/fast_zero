import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fast_zero.app import app
from fast_zero.models import table_registry


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    # engine is the connection to the database
    # in this case, we are using an in-memory SQLite database for testing
    # database will be created and destroyed in memory
    engine = create_engine('sqlite:///:memory:')
    table_registry.metadata.create_all(engine)

    # a session is a temporary connection to the database
    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)
