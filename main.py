import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r'C:\Users\siwar.bouhamed\AppData\Local\Mozilla Firefox\firefox.exe'
# driver = webdriver.Firefox(executable_path="D:\\geckodriver.exe", options=options)

driver = webdriver.Chrome()


driver.maximize_window()
driver.get("http://automationpractice.com/index.php")
print(driver.title)
print(driver.current_url)

time.sleep(5.4)


driver.find_element_by_id().click()

time.sleep(5.4)
driver.close()