from Equal_Experts.TestCase                   import TestCase
from Equal_Experts.Constants                  import EE_Constants
from Equal_Experts.pages.NewSnippetPage       import NewSnippetPage
from Equal_Experts.pages.SignInPage           import SignInPage
import unittest
import time
import nose

class NewSnippetTest(TestCase, unittest.TestCase):

    def setUp(self):
        super(NewSnippetTest, self).setUp()
        super(NewSnippetTest, self).SignIn()
    
    def test_CreateNewSnippet(self):
        action = SignInPage(self.driver, 
                                 EE_Constants['SignIn_Username'],
                                 EE_Constants['SignIn_Password']
        )
        action.SignIn()
        super(NewSnippetTest, self).NewSnippet()
        action = NewSnippetPage(self.driver, 
                                 EE_Constants['NewSnippetContent']
        )
        action.CreateNewSnippet()
        """
        Just using time.sleep() so that you see the last webdriver action.
        I do not recommend using this in your tests.
        """
        time.sleep(5)
    
    def tearDown(self):
        super(NewSnippetTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



