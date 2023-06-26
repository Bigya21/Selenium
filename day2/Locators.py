from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(20)
# driver.find_element(By.ID, "email").send_keys("bigya821@gmail.com")
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("bigya.stha")
# driver.find_element(By.ID, "pass").send_keys("Pass123")
driver.find_element(By.CSS_SELECTOR, "input[id='pass']").send_keys("Pass12")
driver.find_element(By.NAME, "login").click()
act_title = driver.title
exp_title = "Facebook - log in or sign up"
if act_title == exp_title:
    print("Passed")
else:
    print("Failed")
driver.close()
# Build your own computer