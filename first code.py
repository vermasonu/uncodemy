from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
#Sending Data
driver.find_element(By.XPATH,'//input[@name="username"]').send_keys("Admin")
driver.find_element(By.XPATH,'//input[@name="password"]').send_keys("admin123")
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(5)
driver.find_element(By.XPATH,'(//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"])[12]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//textarea[@class="oxd-buzz-post-input"]').send_keys("Sonu")
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(5)

# driver.find_element(By.ID,"")
# driver.find_element(By.CLASS_NAME,"")
# driver.find_element(By.NAME,"")



time.sleep(5)


