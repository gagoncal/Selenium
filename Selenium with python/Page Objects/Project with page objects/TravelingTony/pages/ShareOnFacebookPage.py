from BasePage                import BasePage
from BasePage                import IncorrectPageException


class ShareOnFacebookPage(BasePage):

    def __init__(self, driver):
		super(ShareOnFacebookPage, self).__init__(driver)
  

    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, "name", "share")
        except:   
          raise IncorrectPageException
    
    def share(self):
        self.click(10, "name", "share")