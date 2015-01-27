from TravelingTony.BaseTestCase            import BaseTestCase
from TravelingTony.Constants               import TT_Constants
from TravelingTony.pages.ProductPage       import ProductPage
from TravelingTony.pages.TwitterLoginPage  import TwitterLoginPage



class TestCase(BaseTestCase):

  def setUp(self):
      super(TestCase, self).setUp()
      productPageURL = TT_Constants['Base_URL']+"store/p1/Leatherback_Turtle_Picture.html"
      self.navigate_to_page(productPageURL)
      product_page_obj = ProductPage(self.driver)
      product_page_obj.click_share_on_twitter_button()
      action = TwitterLoginPage(self.driver, 
                                 TT_Constants['Twitter_Username'],
                                 TT_Constants['Twitter_Password']
      )
      action.login()
      

  def tearDown(self):
  	  super(TestCase, self).tearDown()
