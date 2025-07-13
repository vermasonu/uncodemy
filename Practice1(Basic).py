from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Register.html")
time.sleep(5)
driver.find_element(By.XPATH,'//input[@placeholder="First Name"]').send_keys("Sonu")
driver.find_element(By.XPATH,'//input[@placeholder="Last Name"]').send_keys("Verma")
driver.find_element(By.XPATH,"/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/textarea[1]").send_keys("Ward No. 6, kathua")
driver.find_element(By.XPATH,'//input[@type="email"]').send_keys("sonuverma2505@gmail.com")
driver.find_element(By.XPATH,'//input[@type="tel"]').send_keys("9419290571")
driver.find_element(By.XPATH,'//input[@type="radio"][1]').click()
driver.find_element(By.XPATH,'//input[@type="checkbox"][1]').click()
driver.find_element(By.XPATH,'//input[@id="checkbox2"]').click()
driver.find_element(By.XPATH,'//input[@id="firstpassword"]').send_keys("Test@123")
driver.find_element(By.XPATH,'//input[@id="secondpassword"]').send_keys("Test@123")
driver.find_element(By.XPATH,'//button[@id="submitbtn"]').click()
time.sleep(5)
driver.close()