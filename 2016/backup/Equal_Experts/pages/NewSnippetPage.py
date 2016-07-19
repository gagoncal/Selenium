from BasePage                              import BasePage
from MySnippetsPage                        import MySnippetsPage
from BasePage                              import IncorrectPageException
from Equal_Experts.UIMap                   import NewSnippetPageMap
from Equal_Experts.UIMap                   import LoggedInPoductPageMap

class NewSnippetPage(BasePage):

    def __init__(self, driver, NewSnippetContent):
        super(NewSnippetPage, self).__init__(driver)
        self.NewSnippetContent = NewSnippetContent
    
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         LoggedInPoductPageMap['NewSnippetLinkXpath']
          )
        except:   
          raise IncorrectPageException
    
    
    def CreateNewSnippet(self):
      
        self.fill_out_field("xpath", 
                            NewSnippetPageMap['SnippetTextBoxXpath'], 
                            self.NewSnippetContent
        )
        
        self.click(10, 
                   "xpath",
                   NewSnippetPageMap['SubmitButtonXpath'] 
                   
        )
        return MySnippetsPage(self.driver)

    


