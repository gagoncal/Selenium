from BasePage                              import BasePage
from MySnippetsPage                        import MySnippetsPage
from BasePage                              import IncorrectPageException
from Equal_Experts.UIMap                   import UploadCompletedPageMap

class UploadCompletedPage(BasePage):

    def __init__(self, driver):
        super(UploadCompletedPage, self).__init__(driver)
    
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         UploadCompletedPageMap['UploadCompletedTextXpath']
          )
        except:   
          raise IncorrectPageException