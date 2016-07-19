import unittest
import time
from selenium                                   import webdriver
from Equal_Experts.pages.BasePage               import BasePage
from Equal_Experts.pages.ProductPage            import ProductPage


class DatePickerTest(unittest.TestCase):

    def setUp(self):
        #define a driver instance, for example Chrome
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    
    def test_date_picker_input_text(self):
        driver = self.driver
        #navigate to the test website       
        driver.get('https://jqueryui.com/datepicker/')
        time.sleep(3)
        #define frame
        #frame = driver.find_element_by_tag_name('iframe')
        frame = wait_for_element_visibility(10,"tag",'iframe')
        #switch to frame
        driver.switch_to_frame(frame)
        #find date picker
        #datepicker=driver.find_element_by_id('datepicker')
        #datepicker = wait_for_element_visibility(10, 
        #                                 "id", 
        #                                 'datepicker')
        #click on the datepicker to show the calendar
        #datepicker.click()
        self.click(10,"id","datepicker")
        time.sleep(3)
        #Set correct month
        #month = driver.findElement(By.xpath("//span[@class='ui-datepicker-month']")).getText()
        #print month  
        #while()
        #find the day
        #day=driver.find_element_by_xpath("//table/tbody/tr/td/a[text()='15']")
        #day=driver.find_element_by_xpath("//a[contains(text(), '15')]")
        #click on the day
        #day.click()
        self.click(10,"xpath","//a[contains(text(), '15')]")
        time.sleep(5)
        #find datepicker element again
        datepicker=driver.find_element_by_id('datepicker')
        print"date is ",datepicker.get_attribute('value')
        self.assertEqual(datepicker.get_attribute('value'),'02/15/2016')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        
if __name__ == "__main__":
    nose.main()