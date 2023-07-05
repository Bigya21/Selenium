from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service(r"C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

noOfRows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
noOfCols = len(driver.find_elements(By.XPATH, " //table[@name='BookTable']//tr/th"))

print(noOfRows)
print(noOfCols)

data = driver.find_element(By.XPATH, " //table[@name='BookTable']/tbody/tr[3]/td[3]").text
print(data)

# print("All the Rows and Columns....")
# for r in range(2,noOfRows+1):
#     for c in range(1, noOfCols+1):
#         data = driver.find_element(By.XPATH, " //table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data, end = '              ')
#     print()

for r in range(2, noOfRows+1):
    authorName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[2]").text
    if authorName == "Mukesh":
        bookName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print(bookName, "             ", authorName, "            ",price)


driver.close()
