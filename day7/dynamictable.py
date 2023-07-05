from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service(r"C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(3)

driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)

driver.find_element(By.XPATH, "//a[@class='oxd-main-menu-item active']").click()
driver.find_element(By.XPATH, "(//span[normalize-space()='User Management'])[1]").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Admin']").click()
# errorrrr
time.sleep(3)

