from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(10)

driver.find_element(By.CSS_SELECTOR,  "a[href='http://www.orangehrm.com']").click()
time.sleep(10)
# driver.close()
driver.quit()
