from BasePage                import BasePage
from SignUpPage              import SignUpPage
from SignInPage              import SignInPage
from NewSnippetPage          import NewSnippetPage
from Equal_Experts.Constants import EE_Constants
from BasePage                import IncorrectPageException
from Equal_Experts.UIMap     import HomePageMap
from Equal_Experts.UIMap     import LoggedInPoductPageMap

class ProductPage(BasePage):

    def __init__(self, driver):
        super(ProductPage, self).__init__(driver)
  

    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         HomePageMap['SignUpLinkXpath']
          )
        except:   
          raise IncorrectPageException
    
    def click_SignUp_button(self):
        self.click(10, "xpath", HomePageMap['SignUpLinkXpath'])

        return SignUpPage(self.driver, 
                                EE_Constants['SignUp_Username'],
                                EE_Constants['SignUp_Password'] 
        )

    def click_SignIn_button(self):
        self.click(10, "xpath", HomePageMap['SignInLinkXpath'])

        return SignInPage(self.driver, 
                                EE_Constants['SignIn_Username'],
                                EE_Constants['SignIn_Password'] 
        )

    def click_NewSnippet_button(self):
        self.click(10, "xpath", LoggedInPoductPageMap['NewSnippetLinkXpath'])
        return NewSnippetPage(self.driver, 
                                EE_Constants['NewSnippetContent'] 
        )

    

