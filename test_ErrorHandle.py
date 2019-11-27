'''
pytest -v -rx filename
'''

import pytest


def sq():
    return 2*2

def test_zero_division001():
    printer("start server from virtual env")
    with pytest.raises(ZeroDivisionError):
        assert 1 / 0 == 0, "divide 1 by zero"
        print ("hello")

def test_zero_division002():
    with pytest.raises(ZeroDivisionError):
        assert 1 / 1 == 1, ( "Expeted failure as expected  is 1" )

def test_zero_division003():
    input1  = 1/1
    output1 = sq()                        
    with pytest.raises(ZeroDivisionError):
        assert input1 == output1, ( "Expeted failure as expected  is ")
    


@pytest.mark.xfail(reason = "Should not raise error as 1/1 is not zero devision error")
def test_zero_division004():
    with pytest.raises(ZeroDivisionError):
        1 / 1

