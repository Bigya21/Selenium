from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service(r"C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://itera-qa.azurewebsites.net/")
driver.maximize_window()
time.sleep(5)

# Click on Link
driver.find_element(By.LINK_TEXT, 'Practice').click()
time.sleep(5)
driver.find_element(By.PARTIAL_LINK_TEXT, 'Tutor').click()
time.sleep(5)

# Find number of links in the page
links = driver.find_elements(By.TAG_NAME, 'a')
print("Total number of links: ", len(links))

# find all the name of links
for link in links:
    print(link.text)

driver.quit()
