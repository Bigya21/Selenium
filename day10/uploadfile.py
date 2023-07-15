from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

serv_obj = Service(r"C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.foundit.in/")
driver.maximize_window()

driver.find_element(By.XPATH, "//div[@class='heroSection-buttonContainer_secondaryBtn__text']")
driver.find_element(By.XPATH, "//input[@id='file-upload']").send_keys("C:\\Users\\bigya\\Downloads\\BigyaShresthaResume10.pdf")

