from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

serv_obj = Service(r"C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.ID, "dob").click()
datepicker_month = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']"))
datepicker_month.select_by_visible_text("Dec")

datepicker_year = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']"))
datepicker_year.select_by_visible_text("2023")

alldates = driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for date in alldates:
    if date.text == "25":
        date.click()
        break
