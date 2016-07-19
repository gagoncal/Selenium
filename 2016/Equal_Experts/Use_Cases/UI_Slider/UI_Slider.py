import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from Equal_Experts.pages.BasePage               import BasePage

class ActionChainsTests(unittest.TestCase):

    def setUp(self):
        #define a driver instance, for example Chrome
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_slider_drag_drop_offset(self):
        driver = self.driver
        #navigate to the demo website
        driver.get('https://jqueryui.com/slider/#default')
        time.sleep(3)
        #define Frame
        frame=driver.find_element_by_tag_name('iframe')
        #Switch to the frame
        driver.switch_to_frame(frame)
        #define slider

        t=BasePage(driver)
        slider=t.find_element("xpath","//div[@id='slider']/span")
        
        #get x location before dragging and dropping slider
        slider_location_before=slider.location
        x1=slider_location_before.get('x')
        print x1

        #define Action Chains
        actions=ActionChains(driver)
        actions.drag_and_drop_by_offset(slider,300,0)
        actions.perform()
        #Sleep
        time.sleep(5)


        #get x location after dragging and dropping slider
        slider=t.find_element("xpath","//div[@id='slider']/span")
        slider_location_after=slider.location
        x2=slider_location_after.get('x')
        print x2
        #verify that x2 and x1 difference is equal to or greater than 300
        self.assertTrue((x2-x1)>=300)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()