from BasePage                              import BasePage
from AccountCreatedPage                    import AccountCreatedPage
from BasePage                              import IncorrectPageException
from Equal_Experts.UIMap                   import SignUpPageMap

class SignUpPage(BasePage):

    def __init__(self, driver, username, password):
        super(SignUpPage, self).__init__(driver)
        self.username = username
        self.password = password
    
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         SignUpPageMap['UsernameFieldXpath']
          )
        except:   
          raise IncorrectPageException
    
    
    def SignUp(self):
      
        self.fill_out_field("xpath", 
                            SignUpPageMap['UsernameFieldXpath'], 
                            self.username
        )
        self.fill_out_field("xpath", 
                            SignUpPageMap['PasswordFieldXpath'], 
                            self.password
        )
        self.click(10, 
                   "xpath",
                   SignUpPageMap['CreateAccountButtonXpath'] 
                   
        )
        return AccountCreatedPage(self.driver)


