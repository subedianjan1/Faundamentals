import pytest
                        
def test_ZeroError():
    number = [1,2,3,4,5]
    with pytest.raises(ZeroDivisionError):
        for x in number:
            x/0
        

def test_Even():
    eNumber = [2,4,6,8,12]
    for x in eNumber:
        assert  x % 2 == 0

        
def test_Even1():
    eNumber = [2,4,6,8,12]
    for x in eNumber:
        assert  x % 2 == 0
        
