from Equal_Experts.TestCase                   import TestCase
from Equal_Experts.Constants                  import EE_Constants
from Equal_Experts.pages.SignUpPage           import SignUpPage
import unittest
import time
import nose

class SignUpTest(TestCase, unittest.TestCase):

    def setUp(self):
        super(SignUpTest, self).setUp()
        super(SignUpTest, self).SignUp()
        
    def test_SignUpTest(self):
        action = SignUpPage(self.driver, 
                                 EE_Constants['SignIn_Username'],
                                 EE_Constants['SignIn_Password']
        )
        action.SignUp()
        """
        Just using time.sleep() so that you see the last webdriver action.
        I do not recommend using this in your tests.
        """
        time.sleep(5)
    
    def tearDown(self):
        super(SignUpTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



