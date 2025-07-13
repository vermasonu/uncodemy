from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Register.html")
driver.implicitly_wait(2)
driver.save_screenshot('image.png')
driver.quit()