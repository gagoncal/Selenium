import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class ActionChainsTests(unittest.TestCase):

    def setUp(self):
        #define a driver instance, for example Chrome
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_selectable_elements(self):
        driver = self.driver
        #navigate to the demo website
        driver.get('https://jqueryui.com/selectable/')
        time.sleep(2)
        #define Frame
        frame=driver.find_element_by_tag_name('iframe')
        #Switch to the frame
        driver.switch_to_frame(frame)
        #define item 1
        item1=driver.find_element_by_xpath("//ol[@id='selectable']/li[text()='Item 1']")
        #click item 1
        item1.click()
        time.sleep(2)
        #get item 2
        item2=driver.find_element_by_xpath("//ol[@id='selectable']/li[text()='Item 2']")
        #define Action Chains
        actions=ActionChains(driver)
        #press Ctrl Key
        actions.send_keys(Keys.CONTROL)
        #click item2
        actions.click(item2)
        actions.perform()
        #Sleep
        time.sleep(2)
        #get selected items
        selected_items=driver.find_elements_by_xpath("//ol[@id='selectable']/li[contains(@class,'ui-selected')]")
        #get selected items count
        items_count=len(selected_items)
        print 'Selected items:'+str(items_count)
        #verify that 2 items were selected
        self.assertTrue(items_count==2)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()