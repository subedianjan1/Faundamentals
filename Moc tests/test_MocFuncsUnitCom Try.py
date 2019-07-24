'''
Moc test to make sure smmm function is called. although we dont know the
real functionality of methoded may or may not be correct as it is patched
with moc.
Even though threre is 10 secs weait for summ, it takes 0.03 secs for the test to run.
If we do normal test it will take more than 10 secs.

usage: pytest -v test_MocFuncs2.py
or

test_MocFuncs2.py

' testing assert_called_with ', that tests the summ is called correctly with right amount
and type of aruments
For the functon that has no return value this test can be done to make sure
it is called

'''
import time
import unittest
import os
#import unittest from mock
from mock import Mock
import Funcs

from unittest import TestCase
from unittest.mock import patch

class FirstMoc(unittest.TestCase):
    #@patch('Funcs.summ', return_value = 9) #patch the Funcs.summ with Moc stuff
    @patch('Funcs.summ')
    #replacing the real process and provide return value of 9
    def test_Moc_call(self, summ_mock):
        Funcs.summ(2,3) # dont't know why we need to call it here?? but fails if we don't.
        summ_mock.assert_called_with(2,3)# does not test for return value. Tests for the function
        #is called with the correct arguments
        summ_mock.reset_mock()
        result = Funcs.summ(2,4)
        summ_mock.assert_not_called()
         
if __name__== '__main__':
    unittest.main()




