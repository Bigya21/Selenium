from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()
time.sleep(10)

# Select specific checkbox
# driver.find_element(By.XPATH,"//input[@id='monday']").click()

# select all the checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))

# approach 1
for checkbox in checkboxes:
    checkbox.click()

# approach 2
# for i in range(len(checkboxes)):
#     checkboxes[i].click()

# 3
# select multiple check boxes by choice
# for checkbox in checkboxes:
#     weekname = checkbox.get_attribute('id')
#     if weekname =='monday' or weekname == 'sunday':
#         checkbox.click()

# # select last 3 checkboxes
# for i in range(len(checkboxes)-3,len(checkboxes)):
#     checkboxes[i].click()

time.sleep(5)
# clearing all the checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()
