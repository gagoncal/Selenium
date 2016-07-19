import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class ActionsChainsTests(unittest.TestCase):

    def setUp(self):
        #define a driver instance, for example Chrome
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_action_chains_drag(self):
        driver = self.driver
        #navigate to the demo website
        driver.get('https://jqueryui.com/draggable/')
        time.sleep(3)
        #define Frame
        frame=driver.find_element_by_tag_name('iframe')
        #Switch to the frame
        driver.switch_to_frame(frame)
        #define draggable element
        draggable_element=driver.find_element_by_xpath("//div[@id='draggable']")
        #get location before drag
        location1=draggable_element.location
        print "Before Drag Position: ",location1
        #get x position before drag
        x1=location1.get('x')
        print x1
        #define Action Chains
        actions=ActionChains(driver)
        actions.drag_and_drop_by_offset(draggable_element,100,0)
        actions.perform()
        #Sleep
        time.sleep(5)
        #get location after drag
        location2=draggable_element.location
        print "After Drag Position: ",location2
        #get x position after drag
        x2=location2.get('x')
        print x2
        #verify that x position difference is 100
        self.assertTrue(x2-x1==100)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()