from BasePage                import BasePage
from Equal_Experts.Constants import EE_Constants
from BasePage                import IncorrectPageException
from Equal_Experts.UIMap     import LoggedInPoductPageMap
from NewSnippetPage          import NewSnippetPage
from UploadPage              import UploadPage

class LoggedInProductPage(BasePage):

    def __init__(self, driver):
        super(LoggedInProductPage, self).__init__(driver)
  

    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         LoggedInPoductPageMap['UserFieldXpath']
          )
        except:  
          print LoggedInProductPageMap['UserFieldXpath'] 
          raise IncorrectPageException

    

    def click_NewSnippet_button(self):
        self.click(10, "xpath", LoggedInPoductPageMap['NewSnippetLinkXpath'])
        return NewSnippetPage(self.driver, 
                                EE_Constants['NewSnippetContent'] 
        )

    def Click_Upload_button(self):
        self.click(10, "xpath", LoggedInPoductPageMap['UploadLinkXpath'])
        return UploadPage(self.driver, 
                                EE_Constants['Path_To_File']
        )   
