# TEST CASE
# Open Url https://opensource-demo.orangehrmlive.com/
# Enter username(Admin)
# Enter password(admin123)
# Click on Login
# Capture title of the home page(Actual Title)
# Verify title of the page: OrangeHRM (Expected)
# Close Browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
# open web browser
serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
# open url
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(20)
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CLASS_NAME, "oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()
act_title = driver.title
esp_title = "OrangeHRM"
if act_title == esp_title:
    print("passed")
else:
    print("failed")
driver.close()
