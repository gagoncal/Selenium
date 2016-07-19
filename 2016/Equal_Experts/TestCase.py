from Equal_Experts.BaseTestCase                 import BaseTestCase
from Equal_Experts.Constants                    import EE_Constants
from Equal_Experts.pages.ProductPage            import ProductPage
from Equal_Experts.pages.SignUpPage             import SignUpPage
from Equal_Experts.pages.SignInPage             import SignInPage
from Equal_Experts.pages.UploadPage             import UploadPage
from Equal_Experts.pages.NewSnippetPage         import NewSnippetPage 
from Equal_Experts.pages.LoggedInProductPage    import LoggedInProductPage



class TestCase(BaseTestCase):

  def setUp(self):
      super(TestCase, self).setUp()
      productPageURL = EE_Constants['Base_URL']
      self.navigate_to_page(productPageURL)

  def SignUp(self):
      Product_page_obj = ProductPage(self.driver)
      Product_page_obj.click_SignUp_button()
      action = SignUpPage(self.driver, 
                                 EE_Constants['SignUp_Username'],
                                 EE_Constants['SignUp_Password']
        )
      action.SignUp()
  
  def SignIn(self):
      Product_page_obj = ProductPage(self.driver)
      Product_page_obj.click_SignIn_button()
      action = SignInPage(self.driver, 
                                 EE_Constants['SignIn_Username'],
                                 EE_Constants['SignIn_Password']
        )
      action.SignIn()

  def NewSnippet(self):
      LoggedInProductPage_page_obj = LoggedInProductPage(self.driver)
      LoggedInProductPage_page_obj.click_NewSnippet_button()
      action = NewSnippetPage(self.driver, 
                                 EE_Constants['NewSnippetContent']
      )
      action.CreateNewSnippet()

  def Upload(self):
      action = LoggedInProductPage(self.driver)
      action.Click_Upload_button()
      action = UploadPage(self.driver, 
                               EE_Constants['Path_To_File']
      )
      action.UploadFile()

  def tearDown(self):
  	  super(TestCase, self).tearDown()
