from BasePage                import BasePage
from ShareOnTwitterPage      import ShareOnTwitterPage
from BasePage                import IncorrectPageException
from TravelingTony.UIMap     import TwitterLoginPageMap

class TwitterLoginPage(BasePage):

    def __init__(self, driver, username, password):
        super(TwitterLoginPage, self).__init__(driver)
        self.username = username
        self.password = password

    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                           "id", 
                                            TwitterLoginPageMap['UsernameFieldID']
          )
        except:   
          raise IncorrectPageException
    
    def login(self):
        self.fill_out_field("id", 
                            TwitterLoginPageMap['UsernameFieldID'], 
                            self.username
        )
        self.fill_out_field("id", 
                            TwitterLoginPageMap['PasswordFieldID'], 
                            self.password
        )
        self.click(10, 
                   "xpath",
                   TwitterLoginPageMap['SignAndTweetButtonXpath'] 
                   
        )
        return ShareOnTwitterPage(self.driver)


