from BasePage                import BasePage
from BasePage                import IncorrectPageException
from Equal_Experts.UIMap     import MySnippetsPageMap

class MySnippetsPage(BasePage):

    def __init__(self, driver):
        super(MySnippetsPage, self).__init__(driver)


    def _verify_page(self):
        try:
               self.wait_for_element_visibility(10, 
                                           "xpath", 
                                           MySnippetsPageMap['AllSnippetsBoxXpath']
          )
        except:   
          raise IncorrectPageException


