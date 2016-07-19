from BasePage                import BasePage
from BasePage                import IncorrectPageException
from Equal_Experts.UIMap     import AccountCreatedPageMap

class AccountCreatedPage(BasePage):

    def __init__(self, driver):
        super(AccountCreatedPage, self).__init__(driver)


    def _verify_page(self):
        try:
               self.wait_for_element_visibility(10, 
                                           "xpath", 
                                           AccountCreatedPageMap['MessageFieldXpath']
          )
        except:   
          raise IncorrectPageException


