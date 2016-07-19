from Equal_Experts.TestCase                   import TestCase
from Equal_Experts.Constants                  import EE_Constants
from Equal_Experts.pages.SignInPage           import SignInPage
import unittest
import time
import nose

class SignInTest(TestCase, unittest.TestCase):

    def setUp(self):
        super(SignInTest, self).setUp()
        
        
        
    def test_SignInTest(self):
        super(SignInTest, self).SignIn()
        """
        Just using time.sleep() so that you see the last webdriver action.
        """
        time.sleep(5)
    
    def tearDown(self):
        super(SignInTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



