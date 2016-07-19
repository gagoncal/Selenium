import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class ActionChainsTests(unittest.TestCase):

    def setUp(self):
        #define a driver instance, for example Chrome
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_action_chains_drag_drop(self):
        driver = self.driver
        #navigate to the demo website
        driver.get('https://jqueryui.com/droppable/')
        time.sleep(3)
        #define Frame
        frame=driver.find_element_by_tag_name('iframe')
        #Switch to the frame
        driver.switch_to_frame(frame)
        #define draggable element
        draggable_element=driver.find_element_by_xpath("//div[@id='draggable']")
        #define droppable element
        droppable_element=driver.find_element_by_xpath("//div[@id='droppable']")
        #define Action Chains
        actions=ActionChains(driver)
        actions.drag_and_drop(draggable_element,droppable_element)
        actions.perform()
        #Sleep
        time.sleep(5)
        #get draggable location
        draggable_location=draggable_element.location
        print "Draggable Position: ",draggable_location
        #get x position of draggable
        drag_x=draggable_location.get('x')
        print drag_x
        #get droppable location
        droppable_location=droppable_element.location
        print "Droppable Position: ",droppable_location
        #get x position of droppable element
        drop_x=droppable_location.get('x')
        print drop_x
        #verify that drag_x is greater than drop_x
        self.assertTrue(drag_x>drop_x)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()