from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r'C:\Users\siwar.bouhamed\AppData\Local\Mozilla Firefox\firefox.exe'
# driver = webdriver.Firefox(executable_path="D:\\geckodriver.exe", options=options)

driver = webdriver.chrome(executable_path="D:\\chromedriver.exe")


driver.maximize_window()
driver.get("https://www.google.com/")
print(driver.title)
print(driver.current_url)
driver.get("https://stackoverflow.com/")
print(driver.title)
driver.minimize_window()
driver.back()
# driver.refresh()
driver.close()