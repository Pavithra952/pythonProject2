import pytest

@pytest.fixture
def input_value():
    input=39
    return input
def test_divisible_by_3(input_value):
    assert input