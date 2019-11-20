'''
pytest -v -rx filename
'''

import pytest

def test_zero_division001():
    with pytest.raises(ZeroDivisionError):
        1 / 0


@pytest.mark.xfail(reason = "Should not raise error as 1/1 is not zero devision error")
def test_zero_division002():
    with pytest.raises(ZeroDivisionError):
        1 / 1

