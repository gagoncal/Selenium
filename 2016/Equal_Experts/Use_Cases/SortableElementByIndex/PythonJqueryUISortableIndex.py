import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class ActionChainsTests(unittest.TestCase):

    def setUp(self):
        #define a driver instance, for example Chrome
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_Sortable_elements_By_Index(self):
        driver = self.driver
        #navigate to the demo website
        driver.get('http://jqueryui.com/sortable/')
        time.sleep(5)
        #define Frame
        frame=driver.find_element_by_tag_name('iframe')
        #Switch to the frame
        driver.switch_to_frame(frame)
        #define item 1
        item1=driver.find_element_by_xpath("//ul[@id='sortable']/li[text()='Item 1']")
        item_height=item1.size.get('height')
        #define Action Chains
        actions=ActionChains(driver)
        #item1 drag and drop by offset
        actions.drag_and_drop_by_offset(item1,0,item_height+10)
        #perform actions
        actions.perform()
        #Sleep
        time.sleep(5)
        #get all items
        all_items=driver.find_elements_by_xpath("//ul[@id='sortable']/li[contains(text(),'Item')]")
        number_of_items=len(all_items)
        print "Number of Items: ",number_of_items
        #define a list that contains all the text of the items
        items_text=[]
        #Loop all items to get each item's text
        for item in all_items:
            items_text.append(item.text)
            print item.text
        #get item 2 and item 1 index
        item2_index=items_text.index('Item 2')
        item1_index=items_text.index('Item 1')
        print "Item2 index ",item2_index, "Item 1 index ",item1_index
        self.assertTrue(item1_index>item2_index)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()