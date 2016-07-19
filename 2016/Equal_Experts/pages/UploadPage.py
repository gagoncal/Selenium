from BasePage                              import BasePage
from UploadCompletedPage                   import UploadCompletedPage
from BasePage                              import IncorrectPageException
from Equal_Experts.UIMap                   import LoggedInPoductPageMap
from Equal_Experts.UIMap                   import UploadPageMap
import pywinauto

class UploadPage(BasePage):

    def __init__(self, driver, Path_To_File):
        super(UploadPage, self).__init__(driver)
        self.Path_To_File = Path_To_File
    
    def _verify_page(self):
        try:
          self.wait_for_element_visibility(10, 
                                         "xpath", 
                                         LoggedInPoductPageMap['UploadLinkXpath']
          )
        except:   
          raise IncorrectPageException
    
    
    def UploadFile(self):

        self.click(10,
                   "xpath", 
                    UploadPageMap['UploadFieldXpath']
        )
        app = pywinauto.application.Application()
        #mainWindow = app['Carregar Ficheiro'] # main windows' title
        mainWindow = app['Open'] # main windows' title
        ctrl=mainWindow['Edit'] 
        mainWindow.SetFocus()
        ctrl.ClickInput()
        ctrl.TypeKeys(self.Path_To_File)
        ctrlBis = mainWindow['Open'] # open file button
        ctrlBis.ClickInput()
        self.click(10, 
                   "xpath",
                   UploadPageMap['UploadButtonXpath'] 
                   
        )    

        return UploadCompletedPage(self.driver)

    


