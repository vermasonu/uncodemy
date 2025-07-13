from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.maximize_window()
time.sleep(2)
actions=ActionChains(driver)
driver.find_element(By.XPATH,"//button[@class='btn btn-danger']").click()
alert=driver.switch_to.alert
alert.accept()
driver.find_element(By.XPATH,"//a[normalize-space()='Alert with OK & Cancel']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-primary']").click()
alert=driver.switch_to.alert
alert.dismiss()
driver.find_element(By.XPATH,"//a[normalize-space()='Alert with Textbox']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-info']").click()
alert=driver.switch_to.alert
alert.send_keys("hello")
alert.accept()
time.sleep(10)