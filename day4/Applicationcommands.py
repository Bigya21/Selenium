from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # opening the application URL
time.sleep(20)

print(driver.title)  # to capture the title of the current webpage
print(driver.current_url)  # to capture the url of the current webpage
print(driver.page_source)   # to capture the source code of the page