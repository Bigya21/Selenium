from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("http://www.automationpractice.pl/index.php")
driver.maximize_window()
time.sleep(20)

# Absolute xpath
# driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]").send_keys("T-shirts")
# driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button").click()

# Relative xpath
# driver.find_element(By.XPATH, "//*[@id='search_query_top']").send_keys("T-shirts")
# driver.find_element(By.XPATH, "//*[@id='searchbox']/button").click()
# time.sleep(10)

# Relative xpath with Or operator
# driver.find_element(By.XPATH, "//input[@id='search_query_top' or @placeholder='Search']").send_keys("T-shirts")
# driver.find_element(By.XPATH, "//button[@type='submit' or @class='btn btn-default button-search']").click()
# time.sleep(10)


# Relative xpath with And operator
# driver.find_element(By.XPATH, "//input[@id='search_query_top' and @placeholder='Search']").send_keys("T-shirts")
# driver.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-default button-search']").click()
# time.sleep(10)

# Relative xpath with 'contains' and starts-with operator
driver.find_element(By.XPATH, "//input[contains(@id,'search')]").send_keys("T-shirts")
driver.find_element(By.XPATH, "//button[starts-with(@name,'submit_')]").click()
time.sleep(10)