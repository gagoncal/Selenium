from BasePage                import BasePage
from ShareOnTwitterPage     import ShareOnTwitterPage
from BasePage                import IncorrectPageException


class TwitterLoginPage(BasePage):

    def __init__(self, driver, username, password):
        super(TwitterLoginPage, self).__init__(driver)
        self.username = username
        self.password = password

    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                           "id", 
                                           "username_or_email"
          )
        except:   
          raise IncorrectPageException
    
    def login(self):
        self.fill_out_field("id", 
                            "username_or_email", 
                            self.username
        )
        self.fill_out_field("id", 
                            "password", 
                            self.password
        )
        self.click(10, "xpath", "//input[@type='submit']")
        return ShareOnTwitterPage(self.driver)
        
        
    
      
    




