import unittest
import time
from selenium import webdriver
from Equal_Experts.pages.BasePage               import BasePage
from selenium.common.exceptions                 import NoSuchElementException
from nose.plugins.attrib                        import attr


class JqueryUiTests(unittest.TestCase):

    def setUp(self):
        #define a driver instance, for example Chrome
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_spinner_up(self):
        driver = self.driver
        #navigate to the demo website
        driver.get('https://jqueryui.com/spinner/')
        time.sleep(3)
        #define Frame
        frame=driver.find_element_by_tag_name('iframe')
        #Switch to the frame
        driver.switch_to_frame(frame)
        #define spinner
        spinner_up=driver.find_element_by_xpath("//a[contains(@class,'ui-spinner-up')]")
        #click spinner up 3 times
        spinner_up.click()
        time.sleep(2)
        spinner_up.click()
        time.sleep(2)
        spinner_up.click()
        time.sleep(2)
        #define spinner input box
        spinner_input=driver.find_element_by_xpath("//input[@id='spinner']")
        spinner_value=spinner_input.get_attribute('aria-valuenow')
        print "Value is: ",spinner_value
        self.assertEqual(spinner_value,str(3))

    def test_spinner_down(self):
        driver = self.driver
        #navigate to the demo website
        driver.get('https://jqueryui.com/spinner/')
        time.sleep(3)
        #define Frame
        frame=driver.find_element_by_tag_name('iframe')
        #Switch to the frame
        driver.switch_to_frame(frame)
        #define spinner
        spinner_down=driver.find_element_by_xpath("//a[contains(@class,'ui-spinner-down')]")
        #click spinner down 2 times
        spinner_down.click()
        time.sleep(2)
        spinner_down.click()
        time.sleep(2)
        #define spinner input box
        spinner_input=driver.find_element_by_xpath("//input[@id='spinner']")
        spinner_value=spinner_input.get_attribute('aria-valuenow')
        print "Value is: ",spinner_value
        self.assertEqual(spinner_value,str(-2))

    def test_toggle_Button_disable_enable(self):
        driver = self.driver
        #navigate to the demo website
        driver.get('https://jqueryui.com/spinner/')
        time.sleep(3)
        #define Frame
        frame=driver.find_element_by_tag_name('iframe')
        t = BasePage(driver)
        #Switch to the frame
        driver.switch_to_frame(frame)
        
        #define toggle button
        toggle_button=t.find_element("xpath","//button[@id='disable']")
        #define spinner
        spinner=t.find_element("xpath","//input[contains(@class,'ui-spinner-input')]")

        print "Button is enabled = : ",spinner.is_enabled()
        time.sleep(2)
        self.assertEqual(spinner.is_displayed(),True)
        #click button and disable spinner
        toggle_button.click()
        print "Button is enabled = : ",spinner.is_enabled()
        time.sleep(2)
        self.assertEqual(spinner.is_enabled(),False)

    def test_widget_disable_enable(self):
        driver = self.driver
        #navigate to the demo website
        driver.get('https://jqueryui.com/spinner/')
        time.sleep(3)
        #define Frame
        frame=driver.find_element_by_tag_name('iframe')
        t = BasePage(driver)
        #Switch to the frame
        driver.switch_to_frame(frame)
        
        #define toggle button
        widget_button=t.find_element("xpath","//button[@id='destroy']")
        #define spinner
        spinner_down=t.find_element("xpath","//a[contains(@class,'ui-spinner-down')]")
        print "Button is: ",spinner_down.is_displayed()
        time.sleep(2)
        self.assertEqual(spinner_down.is_displayed(),True)
        #click button and disable spinner
        widget_button.click()
        try:
            print "Button is: ",spinner_down.is_displayed()
            time.sleep(2)
            self.assertEqual(spinner_down.is_displayed(),False)
        except:
            print "Button is: NOT PRESENT"
            time.sleep(2)
    
    
    def test_Get_Value(self):
        driver = self.driver
        #navigate to the demo website
        driver.get('https://jqueryui.com/spinner/')
        time.sleep(3)
        #define Frame
        frame=driver.find_element_by_tag_name('iframe')
        t = BasePage(driver)
        #Switch to the frame
        driver.switch_to_frame(frame)
        
        #define Get Value button
        getValue_button=t.find_element("xpath","//button[@id='getvalue']")

        #Enter Value
        spinner=t.find_element("xpath","//input[contains(@class,'ui-spinner-input')]")
        t.fill_out_field("xpath","//input[contains(@class,'ui-spinner-input')]","1000")

        #click button
        getValue_button.click()
        time.sleep(3)
        #switch to popup

        alert = driver.switch_to_alert()

        print dir(alert)
        print 'Text is', alert.text

        #Accept Alert
        alert.accept

        """
        #Switch to new window
        mainWindowHandle  = driver.window_handles

        #click button
        getValue_button.click()
        allWindowsHandles = driver.window_handles
        for handle in allWindowsHandles:
            if handle != mainWindowHandle[0]:
                driver.switch_to_window(handle)
            break
        """
        #Verify that    the window is displayed
    
    @attr(priority=1)    
    def test_Set_Value(self):

        driver = self.driver
        #navigate to the demo website
        driver.get('https://jqueryui.com/spinner/')
        time.sleep(3)
        #define Frame
        frame=driver.find_element_by_tag_name('iframe')
        t = BasePage(driver)
        #Switch to the frame
        driver.switch_to_frame(frame)
        
        #define Get Value button
        setValue_button=t.find_element("xpath","//button[@id='setvalue']")

        #click button
        setValue_button.click()
        time.sleep(3)
        spinner_input=driver.find_element_by_xpath("//input[@id='spinner']")
        spinner_value=spinner_input.get_attribute('aria-valuenow')
        print "Value is: ",spinner_value
        self.assertEqual(spinner_value,str(5))


    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        
if __name__ == "__main__":
    nose.main()