from BasePage                import BasePage
from BasePage                import IncorrectPageException
from Equal_Experts.UIMap     import LoggedInPoductPageMap

class LoggedInPoductPage(BasePage):

    def __init__(self, driver):
        super(LoggedInPoductPage, self).__init__(driver)


    def _verify_page(self):
        try:
               self.wait_for_element_visibility(10, 
                                           "xpath", 
                                           LoggedInPoductPageMap['UserFieldXpath']
          )
        except:   
          raise IncorrectPageException

    


