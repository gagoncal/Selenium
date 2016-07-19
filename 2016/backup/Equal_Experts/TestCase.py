from Equal_Experts.BaseTestCase                 import BaseTestCase
from Equal_Experts.Constants                    import EE_Constants
from Equal_Experts.pages.ProductPage            import ProductPage
from Equal_Experts.pages.LoggedInProductPage    import LoggedInProductPage



class TestCase(BaseTestCase):

  def setUp(self):
      super(TestCase, self).setUp()
      productPageURL = EE_Constants['Base_URL']
      self.navigate_to_page(productPageURL)

  def SignUp(self):
      Product_page_obj = ProductPage(self.driver)
      Product_page_obj.click_SignUp_button()
  
  def SignIn(self):
      Product_page_obj = ProductPage(self.driver)
      Product_page_obj.click_SignIn_button()

  def NewSnippet(self):
      LoggedInProductPage_page_obj = LoggedInProductPage(self.driver)
      LoggedInProductPage_page_obj.click_NewSnippet_button()

  def Upload(self):
      LoggedInProductPage_page_obj = LoggedInProductPage(self.driver)
      LoggedInProductPage_page_obj.Click_Upload_button()

  def tearDown(self):
  	  super(TestCase, self).tearDown()
