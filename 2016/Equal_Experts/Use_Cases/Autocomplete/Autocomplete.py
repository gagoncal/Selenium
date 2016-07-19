import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from Equal_Experts.pages.BasePage               import BasePage
from nose.plugins.attrib                        import attr


class JqueryUiTests(unittest.TestCase):

    def setUp(self):
        #define a driver instance, for example Chrome
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

 
    def test_auto_complete_displayed(self):
        driver = self.driver
        #navigate to the demo website
        driver.get('https://jqueryui.com/autocomplete/')
        time.sleep(3)
        #define Frame
        frame=driver.find_element_by_tag_name('iframe')
        #Switch to the frame
        driver.switch_to_frame(frame)
        #define input field to for the Auto Complete
        t = BasePage(driver)
        input_field=t.find_element("xpath","//input[@id='tags']")
        time.sleep(2)
        input_field.send_keys('ja')
        time.sleep(2)
        #define auto complete message
        message=t.find_element("xpath","//div[@class='ui-menu-item-wrapper' and contains(text(),'Java')]")
        #verify that the message is displayed
        self.assertTrue(message.is_displayed())

    @attr(priority=1)
    def test_auto_complete_selected(self):
        driver = self.driver
        #navigate to the demo website
        driver.get('https://jqueryui.com/autocomplete/')
        time.sleep(3)
        #define Frame
        frame=driver.find_element_by_tag_name('iframe')
        #Switch to the frame
        driver.switch_to_frame(frame)
        t = BasePage(driver)
        #define input field to for the Auto Complete
        input_field=t.find_element("xpath","//input[@id='tags']")
        time.sleep(2)
        input_field.send_keys('ja')
        time.sleep(2)
        #define auto complete message
        message=t.find_element("xpath","//div[@class='ui-menu-item-wrapper' and contains(text(),'Java')]")
        message.click()
        time.sleep(3)
        #verify that the clicked text is in the input field
        input_text=input_field.get_attribute('value')
        print input_text
        self.assertEqual(input_text,'Java')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()