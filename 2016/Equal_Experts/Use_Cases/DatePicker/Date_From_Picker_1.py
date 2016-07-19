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
        t=BasePage(driver)
        #define frame
        frame = driver.find_element_by_tag_name('iframe')
        driver.switch_to_frame(frame)
        #click on the datepicker to show the calendar
        t.click(10,"id","datepicker")
        time.sleep(3)

        #choose correct month
        #while(month != 'May'):
        run = 0 
        month = t.find_element("xpath","//span[@class='ui-datepicker-month']")
        year = t.find_element("xpath","//span[@class='ui-datepicker-year']")
        #print month.get_attribute('value')
        
        while True:
            if (year.text == "2015") and (month.text == "May"):
                break
            t.click(10,"xpath","//a[@class='ui-datepicker-prev ui-corner-all']")
            month = t.find_element("xpath","//span[@class='ui-datepicker-month']")
            year = t.find_element("xpath","//span[@class='ui-datepicker-year']")

        
        #find the day
        t.click(10,"xpath","//a[contains(text(), '15')]")
        time.sleep(5)  
        #find datepicker element again
        #datepicker=driver.find_element_by_id('datepicker')
        #t.wait_for_element_visibility(10,"id",'iframe'))
        datepicker = t.find_element("id","datepicker")
        
        print "date is ",datepicker.get_attribute('value')
        self.assertEqual(datepicker.get_attribute('value'),'05/15/2015')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        
if __name__ == "__main__":
    nose.main()