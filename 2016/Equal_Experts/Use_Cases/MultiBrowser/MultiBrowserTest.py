from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
from selenium.webdriver.common.keys import Keys

##get the second argument, which is the browser 
browser=str(sys.argv[1])
##print argument browser
print(browser)
##select browser based on the argument
if(browser=="firefox"):
        driver=webdriver.Firefox()
else:
        driver=webdriver.Chrome()
## navigate to the site
driver.get("http://demo.mahara.org/")
## print website title
print(driver.title)
## username field
username = driver.find_element_by_id("login_login_username")
username.send_keys("student2")
## password field
password=driver.find_element_by_id("login_login_password")
password.send_keys("Testing1")
## login button
loginbutton=driver.find_element_by_id("login_submit")
loginbutton.click()
## logout link
logoutlink=driver.find_element_by_link_text("Logout")
## verify logout link
isLogoutDisplayed=logoutlink.is_displayed()
print(isLogoutDisplayed)
## click logout link
logoutlink.click()
## wait until submit button displayed
wait = WebDriverWait(driver, 10)
submitElement = wait.until(EC.presence_of_element_located((By.ID,'login_submit')))
## close the driver
driver.close()
driver.quit()