import sys
import pytest
import math
###########################################

def yep(n):
    if n == 1: 
        return True
    else:
        return False

######################################


#Test Cases:


def testEqual_01():
    assert  2*2 == 5, "Expected fail"

def testNotEqual_02():
    assert 2*2 != 5

def testLessThan_03():
    assert 2*2 < 5
   
def testRange_031():
    x = 5
    assert 1 <= x <= 9

       
@pytest.mark.xfail(reason = "Expected cause lk is not in Hello")#reason bit not working
def testinString_04():
    assert 'lk' in ('hello', "Expected fail")
   # pytest.fail("not configured: {}".format(x))
    pytest.fail("not configured: {}")

#def testTrue():
#    assert yep(1)== True

@pytest.mark.skipif(1!=2, reason="Incorrect recieved")#reason bit not printing
def testSkipif_05():
    assert 1 == 1

print ('*******************************************************')


