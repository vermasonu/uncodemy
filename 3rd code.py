import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("https://www.flipkart.com/")
time.sleep(5)
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH, '//img[@style="width:100%;margin:auto;display:block;position:absolute;top:0;left:0;bottom:0;right:0;padding:inherit;object-fit:contain;opacity:0;aspect-ratio:1/1"]').click()
actions=ActionChains(driver)
