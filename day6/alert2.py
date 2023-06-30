from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service(r"C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://mypage.rediff.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@value=' Go ']").click()
time.sleep(2)

mywindow= driver.switch_to.alert
mywindow.accept()