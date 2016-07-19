from BasePage                              import BasePage
from LoggedInProductPage                   import LoggedInProductPage
from BasePage                              import IncorrectPageException
from Equal_Experts.UIMap                   import SignInPageMap

class SignInPage(BasePage):

    def __init__(self, driver, username, password):
        super(SignInPage, self).__init__(driver)
        self.username = username
        self.password = password
    
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         SignInPageMap['UsernameFieldXpath']
          )
        except:   
          raise IncorrectPageException
    
    
    def SignIn(self):
      
        self.fill_out_field("xpath", 
                            SignInPageMap['UsernameFieldXpath'], 
                            self.username
        )
        self.fill_out_field("xpath", 
                            SignInPageMap['PasswordFieldXpath'], 
                            self.password
        )
        self.click(10, 
                   "xpath",
                   SignInPageMap['LoginButtonXpath'] 
                   
        )
        return LoggedInProductPage(self.driver)


