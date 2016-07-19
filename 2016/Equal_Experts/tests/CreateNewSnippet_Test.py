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
        super(NewSnippetTest, self).NewSnippet()        
        """
        Just using time.sleep() so that you see the last webdriver action.

        """
        time.sleep(5)
    
    def tearDown(self):
        super(NewSnippetTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()



