import unittest
import time
from selenium import webdriver

class JqueryUiTests(unittest.TestCase):

    def setUp(self):
        #define a driver instance, for example Chrome
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        #navigate to the demo website
        self.driver.get('https://jqueryui.com/tabs/')
        time.sleep(3)
        #define Frame
        frame=self.driver.find_element_by_tag_name('iframe')
        #Switch to the frame
        self.driver.switch_to_frame(frame)

    def get_tab(self,tab_number):
        #define tabs
        tabs='tabs-'+str(tab_number)
        tab=self.driver.find_element_by_xpath("//div[@id='tabs']/ul/li[@aria-controls='"+tabs+"']")
        return tab

    def test_tab2(self):
        tab=self.get_tab(2)
        tab.click()
        time.sleep(5)
        #get tab expanded property
        is_tab_expanded=tab.get_attribute('aria-expanded')
        print "Is tab 2 expanded", is_tab_expanded
        self.assertTrue(is_tab_expanded)

    def test_tab3(self):
        tab=self.get_tab(3)
        tab.click()
        time.sleep(5)
        #get tab expanded property
        is_tab_expanded=tab.get_attribute('aria-expanded')
        print "Is tab 3 expanded", is_tab_expanded
        self.assertTrue(is_tab_expanded)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()