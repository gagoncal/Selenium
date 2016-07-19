import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class ActionChainsTests(unittest.TestCase):

    def setUp(self):
        #define a driver instance, for example Chrome
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_action_chains_drag_drop_resize_element(self):
        driver = self.driver
        #navigate to the demo website
        driver.get('https://jqueryui.com/resizable/')
        time.sleep(3)
        #define Frame
        frame=driver.find_element_by_tag_name('iframe')
        #Switch to the frame
        driver.switch_to_frame(frame)
        #define resizable element
        resizable_element=driver.find_element_by_xpath("//div[@id='resizable']/h3")
        #get x size
        x=resizable_element.size.get('width')
        print x
        #define element dragging point for resize 
        dragging_point=driver.find_element_by_xpath("//div[@id='resizable']/div[contains(@class,'ui-icon-gripsmall-diagonal-se')]")
        #define Action Chains
        actions=ActionChains(driver)
        #click and hold the dragging point
        actions.click_and_hold(dragging_point)
        #drag and drop by offset
        actions.drag_and_drop_by_offset(dragging_point,100,0)
        time.sleep(2)
        actions.drag_and_drop_by_offset(dragging_point,100,0)
        actions.perform()
        #Sleep
        time.sleep(5)
        #get width after resizing
        new_x=resizable_element.size.get('width')
        print new_x
        #verify that the difference between new_x and x is 200
        self.assertTrue(new_x-x==200)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()