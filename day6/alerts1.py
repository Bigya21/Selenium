from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service(r"C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()


# for the last alert button
# driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
# time.sleep(5)
#
# alertwindow = driver.switch_to.alert
# print(alertwindow.text)
# alertwindow.send_keys("Selenium")
#
# # alertwindow.accept()
# alertwindow.dismiss()
# time.sleep(3)

# for the seond alert button
driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']").click()
time.sleep(3)

alertwindow = driver.switch_to.alert
alertwindow.accept()
time.sleep(3)