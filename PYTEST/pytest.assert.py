import pytest
def test_d1():
    assert 10+5==15
def test_d2():
    assert 10-5==5
@pytest.mark.skip
def test_d3():
    assert 10+50==60
