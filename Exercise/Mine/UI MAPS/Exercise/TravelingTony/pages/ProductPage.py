from BasePage                import BasePage
from TwitterLoginPage        import TwitterLoginPage
from TravelingTony.Constants import TT_Constants
from BasePage                import IncorrectPageException
from TravelingTony.UIMap     import ProductPageMap

class ProductPage(BasePage):

    def __init__(self, driver):
        super(ProductPage, self).__init__(driver)
  

    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "id", 
                                         ProductPageMap['QuantityDropDownID']
          )
        except:   
          raise IncorrectPageException
    
    def click_share_on_twitter_button(self):
        mainWindowHandle = self.driver.window_handles
        self.click(10, "xpath", ProductPageMap['TwitterShareLinkXpath'])
        allWindowHandles = self.driver.window_handles
        for handle in allWindowHandles:
         if handle != mainWindowHandle[0]:
          self.switch_to_window(handle)
          break
        return TwitterLoginPage(self.driver, 
                                TT_Constants['Twitter_Username'],
                                TT_Constants['Twitter_Password'] 
        )

    

