import unittest
import xml.etree.ElementTree as ET
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


tree=ET.parse('SiteElement.xml')
root=tree.getroot()

def getSearchValue(pagenameattribute,elementkeystring):
    xpathstring="./pages/page[@name='"+pagenameattribute+"']/element[@Key='"+elementkeystring+"']"
    ##print(xpathstring)
    for element in root.findall(xpathstring):
        value=element.find('value').text
        return value
    
def getSearchBy(pagenameattribute,elementkeystring):
    xpathstring="./pages/page[@name='"+pagenameattribute+"']/element[@Key='"+elementkeystring+"']"
    ##print(xpathstring)
    for element in root.findall(xpathstring):
        searchby=element.find('searchby').text
        return searchby
    
class DemoMaharaOrgLogin(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_login_in_demo_mahara_org(self):
        driver = self.driver
        driver.get("http://demo.mahara.org/")
        self.assertIn("Home - Mahara", driver.title)
        username = driver.find_element_by_id(getSearchValue("LoginPage","LoginUserName"))
        username.send_keys("student1")
        password=driver.find_element_by_id(getSearchValue("LoginPage","LoginPassword"))
        password.send_keys("Testing1")
        loginbutton=driver.find_element_by_id(getSearchValue("LoginPage","SubmitButton"))
        loginbutton.click()
        #self.assertTrue(driver.find_element_by_link_text(getSearchValue("DashboardPage","LogoutLink")),"Logout link")
       
    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    nose.main()