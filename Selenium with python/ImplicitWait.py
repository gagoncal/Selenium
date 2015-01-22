from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(15)
driver.get("http://www.google.com")
searchfield = driver.find_element_by_css_selector("input[name=q]")
driver.quit()