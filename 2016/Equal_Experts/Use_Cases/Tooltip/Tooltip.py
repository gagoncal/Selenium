import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from Equal_Experts.pages.BasePage               import BasePage

class JqueryUiTests(unittest.TestCase):

    def setUp(self):
        #define a driver instance, for example Chrome
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_tooltip(self):
        driver = self.driver
        #navigate to the demo website
        driver.get('https://jqueryui.com/tooltip/')
        time.sleep(3)
        #define Frame
        frame=driver.find_element_by_tag_name('iframe')
        #Switch to the frame
        driver.switch_to_frame(frame)
        t = BasePage(driver)

        #define input field to display tool tip
        tooltip_input=t.find_element("xpath","//input[@id='age']")
        #define Action Chains
        actions=ActionChains(driver)
        actions.move_to_element(tooltip_input)
        actions.perform()
        time.sleep(5)
        #define tool tip message element
        tooltip_message=t.find_element("xpath","//div[@role='tooltip']")
        message=tooltip_message.text
        print "Tooltip Message is: ",message
        self.assertEqual(message,'We ask for your age only for statistical purposes.')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()