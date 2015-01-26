from selenium                           import webdriver

from selenium.webdriver.support.ui      import WebDriverWait

from selenium.webdriver.common.by       import By

from selenium.webdriver.support.select  import Select

import unittest




class SwitchToWindow(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://travelingtony.weebly.com/store/p1/Leatherback_Turtle_Picture.html")
        driver.maximize_window()
     
    def test_SwitchToFacebookWindow(self):
        #Locators
        twitterSharingLinkLocator   = "a.wsite-com-product-social-twitter"
        twitterUsernameFieldID      = "username_or_email"
        twitterPasswordFieldID      = "password"
        twitterLoginButtonName      = "login"
        twitterShareLinkButton      = "input[type='submit']"
        
        #Facebook credentials.
        twitterUsername             = "tutorys123@gmail.com"
        twitterPassword             = "year2014"
        
        twSharingLinkElement = WebDriverWait(driver, 10).\
                        until(lambda driver: driver.find_element_by_css_selector(twitterSharingLinkLocator))
         
        # Get the main Window handle
        mainWindowHandle = driver.window_handles
        print "main Window handle: %s" %mainWindowHandle
             
        # Click the "Facebook sharing" link, switch to the Facebook login window and log in
        twSharingLinkElement.click()
        allWindowsHandlesList = driver.window_handles #gives a list of all the windows handles of the session
        print "all window handles: %s" %allWindowsHandlesList
        for handle in allWindowsHandlesList:
            if handle != mainWindowHandle[0]:
               driver.switch_to.window(handle)
               break
        twitterUsernameFieldElement   = WebDriverWait(driver, 10).\
                                       until(lambda driver: driver.find_element_by_id(twitterUsernameFieldID))
        
        twitterPasswordFieldElement   = WebDriverWait(driver, 10).\
                                       until(lambda driver: driver.find_element_by_id(twitterPasswordFieldID))
        
        twitterLoginButtonElement     = WebDriverWait(driver, 10).\
                                       until(lambda driver: driver.find_element_by_css_selector(twitterShareLinkButton))
        
        twitterUsernameFieldElement.send_keys(twitterUsername)
        twitterPasswordFieldElement.send_keys(twitterPassword)
        twitterLoginButtonElement.click()
        #WebDriverWait(driver, 10).\
        #until(lambda driver: driver.find_element_by_name(TwitterShareLinkButtonClass))
        
    
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()



