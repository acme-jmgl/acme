import pytest

from app import create_app
from app import routes
from app.store import TodoStore


@pytest.fixture
def client():
    routes.store = TodoStore()
    return create_app().test_client()
