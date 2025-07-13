import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demoblaze.com/")
driver.find_element(By.XPATH,'//a[@id="login2"]' ).click()
time.sleep(5)
driver.find_element(By.XPATH,'//input[@id="loginusername"]').send_keys("admin2505")
driver.find_element(By.XPATH,'//input[@id="loginpassword"]').send_keys("Admin@321")
driver.find_element(By.XPATH,'//button[@onclick="logIn()"]').click()
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.refresh()
time.sleep(5)