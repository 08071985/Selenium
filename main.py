import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.binary_location = r'C:\Users\siwar.bouhamed\AppData\Local\Mozilla Firefox\firefox.exe'
# driver = webdriver.Firefox(executable_path="D:\\geckodriver.exe", options=options)
driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")

#driver = webdriver.Chrome()


driver.maximize_window()
driver.get("http://automationpractice.com/index.php")
print(driver.title)
print(driver.current_url)

time.sleep(2)


driver.find_element_by_id("search_query_top").send_keys("dress")
driver.find_element_by_name("submit_search").click()

select=Select(driver.find_element_by_id("selectProductSort"))
select.select_by_value("price:desc")
#select.select_by_index(1)
time.sleep(2)


element = driver.find_element_by_class_name("product-container")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
time.sleep(2)
driver.find_element_by_class_name("ajax_add_to_cart_button").click()

time.sleep(2)
driver.close()