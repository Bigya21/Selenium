
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By


serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.nopcommerce.com/en/register")
time.sleep(20)

box = driver.find_element(By.XPATH, "//input[@id='FirstName']")
print("Display: ", box.is_displayed())
print("Display: ", box.is_enabled())

# cb = driver.find_element((By.XPATH, "//label[@for='Newsletter']"))
# print(cb.is_selected())


driver.quit()
