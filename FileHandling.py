from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='imagesrc']").send_keys("C://Users//91941//OneDrive//Desktop//1.jpg")
time.sleep(2)

