from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

drpcountry = Select(driver.find_element(By.XPATH, "//select[@id='input-country']"))

# select option from dropdown
drpcountry.select_by_visible_text("India")
# drpcountry.select_by_value("8")
# drpcountry.select_by_index(13)

