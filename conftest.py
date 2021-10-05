import pytest


@pytest.fixture
def false():
    assert False, "=P"
