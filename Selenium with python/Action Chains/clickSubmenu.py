from selenium                                       import webdriver

from selenium.webdriver.support.ui                  import WebDriverWait

from selenium.webdriver.support                     import expected_conditions as EC

from selenium.webdriver.common.by                   import By

from selenium.webdriver.common.action_chains        import ActionChains

import unittest




class ClickSubmenu(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://travelingtony.weebly.com/")
        driver.maximize_window()
    
    
    
    def test_ClickSubmenu(self):
        #Locators
        africaMenuLocator     = "//a[.='Africa']"
        gabonSubmenuLocator   = "//a[contains(@href, 'gabon')]" 
        impalaDivLocator      = "//div[@class='wsite-header']"
        africaMenuElement     = WebDriverWait(driver, 10).\
                                until(lambda driver: driver.find_element_by_xpath(africaMenuLocator))

        actions = ActionChains(driver)
        actions.move_to_element(africaMenuElement)
        actions.click(driver.find_element_by_xpath(gabonSubmenuLocator))
        actions.perform()

        #Another Way to do it
        #actions = ActionChains(driver)
        #actions.move_to_element(africaMenuElement)
        #actions.perform()
        #gabonSubmenuElement = WebDriverWait(driver, 10).\
        #    until(EC.visibility_of_element_located((By.XPATH, gabonSubmenuLocator)))
        #gabonSubmenuElement.click()


        WebDriverWait(driver, 10).\
            until(lambda driver: driver.find_element_by_xpath(impalaDivLocator))
        

    
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()



