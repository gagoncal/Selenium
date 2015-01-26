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
        driver.get("http://travelingtony.weebly.com")
        driver.maximize_window()
    
    
    
    def test_sendKeys(self):
        #Locators
        searchFieldName      = "q"
        turtlePictureLocator = "//div[@title='Leatherback Turtle Picture']"
        quantityLocatorName = "Quantity"



        searchFieldElement   = WebDriverWait(driver, 10).\
                               until(lambda driver: driver.find_element_by_name(searchFieldName))
        
        #Action Chains
        """1 st example
        actions = ActionChains(driver)
        actions.send_keys_to_element(searchFieldElement,"Leatherback")
        actions.send_keys_to_element(searchFieldElement,Keys.ENTER)
        actions.perform()
        """

        actions = ActionChains(driver)
        actions.click(searchFieldElement)
        actions.send_keys("Leatherback")
        actions.send_keys(Keys.ENTER)
        actions.perform()

        
        turtlePictureElement = WebDriverWait(driver, 10).\
            until(lambda driver: driver.find_element_by_xpath(turtlePictureLocator))

        actions.send_keys_to_element(turtlePictureElement,Keys.ENTER)

        quantityFieldElement   = WebDriverWait(driver, 10).\
                               until(lambda driver: driver.find_element_by_name(quantityLocatorName))

        actions.send_keys_to_element(quantityFieldElement,Keys.ENTER)


        for(i=0;i<2;i++):
            actions.send_keys_to_element(quantityFieldElement,Keys.ARROW_DOWN)

        actions.send_keys_to_element(quantityFieldElement,Keys.ENTER)
        actions.perform()
        time.sleep(6)



    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()



