from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
time.sleep(2)
driver.maximize_window()
actions=ActionChains(driver)
driver.find_element(By.XPATH,'//div[@id="ebc23563-adbb-4abd-912a-94cbbda59e55"]/div[2]/div/ul/li[1]/span/a/img').click()

time.sleep(10)