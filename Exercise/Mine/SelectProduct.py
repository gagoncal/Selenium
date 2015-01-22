from selenium                           import webdriver

from selenium.webdriver.support.ui      import WebDriverWait

from selenium.webdriver.common.by       import By

from selenium.webdriver.support.select  import Select

import unittest

import time


class SeveralActions(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://travelingtony.weebly.com")
        driver.maximize_window()
     
    def testSelectQuantity(self):

        #Find by name and enter in the search field value "Leatherback"
        searchFieldLocator = driver.find_element_by_name("q")
        searchFieldLocator.send_keys("Leatherback")
        searchButtonLocator = "span.wsite-search-button"
        searchButtonElement = WebDriverWait(driver, 10).\
                            until(lambda driver: driver.find_element_by_css_selector(searchButtonLocator))
        searchButtonElement.click()

        #Find Image by title using xpath
        imageTitleLocator =  "//div[@title='Leatherback Turtle Picture']"
        imageTitleElement = WebDriverWait(driver, 10).\
                                 until(lambda driver: driver.find_element_by_xpath(imageTitleLocator))
        imageTitleElement.click()

        QuantityIDLocator =  "wsite-com-product-option-Quantity"
        QuantityIDElement = WebDriverWait(driver, 10).\
                                 until(lambda driver: driver.find_element_by_id(QuantityIDLocator))
        Select(QuantityIDElement).select_by_visible_text("3")


    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()



