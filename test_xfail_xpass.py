'''
pytest -v -rxs filename

to get the reason for xfail of skipping

Note: tests can be skipped or xfailed at parametrization 
'''
import pytest

def add(a,b):
    return a+b

def test_normal():
    x=3
    if x==3:
        assert x == 8, "Expected Failed cause value recived is " + str(x)


@ pytest.mark.xfail(reason="bug 110")
def test_xfail():
    assert 3 == 4
    
#Even though we expeted to fail down for this test case, it passes show we recieve
#xpass as the result ( more like unexpected pass??)
@ pytest.mark.xfail(reason="bug 110")
def test_xpass():
    assert 3 == 3
    


@pytest.mark.parametrize("add1,add2,Result",
                         [(1,2,3),
                          (4,5,9),
                          (5,6,11),
                          pytest.param(1,2,4, marks = pytest.mark.xfail ( reason = "expected by AS")),
                          pytest.param(1,1,2, marks = pytest.mark.skip(reason = "just Skipped"))
                                       #can also do skipif
                             ]
                         )

def test_add(add1,add2,Result):
    assert add(add1,add2) == Result
