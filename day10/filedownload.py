from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    return driver

driver = chrome_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()
driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]").click()
