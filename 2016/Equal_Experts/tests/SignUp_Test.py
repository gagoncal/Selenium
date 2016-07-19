from Equal_Experts.TestCase                   import TestCase
from Equal_Experts.Constants                  import EE_Constants
from Equal_Experts.pages.SignUpPage           import SignUpPage
import unittest
import time
import nose

class SignUpTest(TestCase, unittest.TestCase):

    def setUp(self):
        super(SignUpTest, self).setUp()
        
        
    def test_SignUpTest(self):
        super(SignUpTest, self).SignUp()
        """
        Just using time.sleep() so that you see the last webdriver action.
        """
        time.sleep(5)
    
    def tearDown(self):
        super(SignUpTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



