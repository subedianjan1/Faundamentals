import sys 
import pytest

def valid_config():
    confSetting = 0
    return confSetting

#skipping inside the test
def test_test1():
    if  not valid_config():
        pytest.skip("The configuration is not valid")
        assert 1 == 1

#Skipping the overall test
@pytest.mark.skip(reason = 'Skipped tests')
def test_test2():
    assert 2 == 2

#skip over all test if something global is issue as below
@pytest.mark.skipif(sys.version_info < (3,8) , reason = 'this is version 3.7' )
def test_test3():
    assert 2==6

