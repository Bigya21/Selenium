from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)
# driver.implicitly_wait(10)
# driver.get("https://www.google.com/")
#
# searchbox = driver.find_element(By.NAME, "q")
# searchbox.send_keys("Selenium")
# searchbox.submit()
#
# driver.find_element(By.XPATH, "//h3[text()='Selenium']").click()

# explicit wait
serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
mywait = WebDriverWait(driver, 10, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])


driver.get("https://www.google.com/")

searchbox = driver.find_element(By.NAME, "q")
searchbox.send_keys("Selenium")
searchbox.submit()

searchLink = mywait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))
searchLink.click()
driver.quit()