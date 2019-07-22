'''
Moc test to make sure smmm function is called. although we dont know the
real functionality of methoded may or may not be correct as it is patched
with moc.
Even though threre is 10 secs weait for summ, it takes 0.03 secs for the test to run.
If we do normal test it will take more than 10 secs.

usage: pytest -v test_MocFuncs2.py

'''
import time
from mock import Mock
import Funcs

from unittest import TestCase
from unittest.mock import patch


@patch('Funcs.summ', return_value = 9) #patch the Funcs.summ with Moc stuff
    #replacing the real process and provide return value of 9
def test_example(summ):
    result  = summ(2,3)
    assert result, 9

        



