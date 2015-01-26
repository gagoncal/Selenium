from selenium                                       import webdriver

from selenium.webdriver.support.ui                  import WebDriverWait

from selenium.webdriver.common.by                   import By

from selenium.webdriver.common.action_chains        import ActionChains

from selenium.webdriver.common.keys                 import Keys

import unittest

import time


class sendKeys(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://travelingtony.weebly.com/store/p1/Leatherback_Turtle_Picture.html")
        driver.maximize_window()
    
    
    
    def test_sendKeys(self):
        #Locators
        searchFieldName      = "q"
        turtlePictureLocator = "//div[@title='Leatherback Turtle Picture']"
        quantityLocatorID = "//select[@id='wsite-com-product-option-Quantity']"


        quantityFieldElement   = WebDriverWait(driver, 10).\
                               until(lambda driver: driver.find_element_by_xpath(quantityLocatorID))


        actions = ActionChains(driver)
        actions.send_keys_to_element(quantityFieldElement,Keys.ENTER)

        i=0
        while(i<2):
            actions.send_keys_to_element(quantityFieldElement,Keys.ARROW_DOWN)
            i+=1

        actions.send_keys_to_element(quantityFieldElement,Keys.ENTER)
        actions.perform()
        time.sleep(6)



    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()



