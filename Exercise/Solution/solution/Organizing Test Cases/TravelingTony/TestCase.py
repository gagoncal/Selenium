from TravelingTony.BaseTestCase            import BaseTestCase
from TravelingTony.Constants               import TT_Constants
from TravelingTony.Common                  import Common

class TestCase(BaseTestCase):

  def setUp(self):
      super(TestCase, self).setUp()
      productPageURL = TT_Constants['Base_URL']+"store/p1/Leatherback_Turtle_Picture.html"
      self.navigate_to_page(productPageURL)
      common_obj = Common(self.driver)
      # Wait for the "Quantity" drop-down to display
      common_obj.wait_for_element_visibility(10, 
                                             "id", 
                                             "wsite-com-product-option-Quantity"
      )
      # Click the "Twitter" share link and switch to the "Twitter" login page
      mainWindowHandle  = self.driver.window_handles
      common_obj.click(10, "xpath", "//a[@title='Share on Twitter']")
      allWindowsHandles = self.driver.window_handles
      for handle in allWindowsHandles:
        if handle != mainWindowHandle[0]:
          common_obj.switch_to_window(handle)
          break
      #Verify that the Twitter username/email field is displayed
      common_obj.wait_for_element_visibility(10,
                                             "id", 
                                             "username_or_email"
      )
      # Enter Twitter credentials and click the "Sign In and Tweet" button
      common_obj.fill_out_field("id",
                                "username_or_email",
                                TT_Constants['Twitter_Username']
      )
      common_obj.fill_out_field("id", 
                                "password",
                                TT_Constants['Twitter_Password']
      )
      common_obj.click(10, "xpath", "//input[@value='Sign in and Tweet']")
      # Wait for the "Tweet" button to display. We locate the "Tweet" button by value using Css Selector
      common_obj.wait_for_element_visibility(10, 
                                             "cssSelector",
                                             "input[value=Tweet]"
      )
      
      
      
  def tearDown(self):
  	  super(TestCase, self).tearDown()
