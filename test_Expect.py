'''If there are multiple assertions in one test case . If one assert fails, rest
will not execute. If we use expect instead of assert that problem is solved'''

from delayed_assert import expect, assert_expectations

def test_MultAsserts():
    assert 'lt' in ('hello') # fails here, so rest not executed
    assert 'lt' not in ('heelo')
    assert 'll' in ('hello')
    
def test_Expects():
    expect  ( 1==2, "Continues testing after this" ) # fails here, so rest is still executed
    expect  ( 2==2, )
    expect  ( 3==3, )
    expect  ( 4==5, "contines testing after this" ) # fails here and continues
    expect  ( 4==4, )
    expect  ( 'lt' not in ('heelo') )
    assert 'll' in ('hello')
    assert_expectations()
    

