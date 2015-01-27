from BasePage                import BasePage
from BasePage                import IncorrectPageException


class ShareOnTwitterPage(BasePage):

    def __init__(self, driver):
        super(ShareOnTwitterPage, self).__init__(driver)
  

    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                           "xpath", 
                                           "//input[@type='submit']"
          )
        except:   
          raise IncorrectPageException
    
    def share(self):
        self.click(10, 
                    "xpath", 
                    "//input[@type='submit']"
        )