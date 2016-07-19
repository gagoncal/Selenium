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
        super(UploadTest, self).Upload()
        """
        Just using time.sleep() so that you see the last webdriver action.
        """
        time.sleep(5)
    
    def tearDown(self):
        super(UploadTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



