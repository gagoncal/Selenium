from Equal_Experts.TestCase                            import TestCase
from Equal_Experts.Constants                           import EE_Constants
from Equal_Experts.pages.SignInPage                    import SignInPage
from Equal_Experts.pages.UploadPage                    import UploadPage
from Equal_Experts.pages.LoggedInProductPage           import LoggedInProductPage
import unittest
import time
import nose

class UploadTest(TestCase, unittest.TestCase):

    def setUp(self):
        super(UploadTest, self).setUp()
        super(UploadTest, self).SignIn()
        
    def test_UploadTest(self):
        action = SignInPage(self.driver, 
                                 EE_Constants['SignIn_Username'],
                                 EE_Constants['SignIn_Password']
        )
        action.SignIn()
        action = LoggedInProductPage(self.driver)
        super(UploadTest, self).Upload()
        action = UploadPage(self.driver, 
                                 EE_Constants['Path_To_File']
        )
        action.UploadFile()
        """
        Just using time.sleep() so that you see the last webdriver action.
        I do not recommend using this in your tests.
        """
        time.sleep(5)
    
    def tearDown(self):
        super(UploadTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



