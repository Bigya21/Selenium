from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.snapchat.com/")
time.sleep(5)
driver.get("https://www.instagram.com/")
time.sleep(5)

driver.back()
driver.forward()
driver.refresh()

driver.quit()