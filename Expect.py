'''If there are multiple assertions in one test case . If one assert fails, rest
will not execute. If we use expect instead of assert that problem is solved'''


def test_MultAsserts():
    assert 'lt' in ('hello') # fails here, so rest not executed
    assert 'lt' not in ('heelo')
    assert 'll' in ('hello')
    
def test_Expects(expect):
    expect  ( 'lt' in ('hello') )# fails here, so rest not executed
    expect ( 'lt' not in ('heelo') )
    assert 'll' in ('hello')
