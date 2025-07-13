from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
driver= webdriver.Chrome()
driver.get("https://www.kamera-express.nl/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,'//button[@cs-consent="all"]').click()
a=ActionChains(driver)
def login():

    login=driver.find_element(By.XPATH,"//div[@class='header-content-bottom']//button[@class='user-button sf-button--text no-underline sf-button']")
    a.move_to_element(login).perform()
    driver.find_element(By.XPATH,"//div[@class='header-content-bottom']//div[@class='login-cta-container']//a").click()
    driver.find_element(By.XPATH,"//input[@name='username']").send_keys("sonuverma2505@gmail.com")
    driver.find_element(By.XPATH,"//input[@name='password']").send_keys("Navanya@321")
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@id='btn_login']").click()
    time.sleep(3)
def product():
    prod=driver.find_element(By.XPATH,'(//i[@class="K1-icon-down K1-icon-sm"])[1]')
    a.move_to_element(prod).perform()
    time.sleep(3)
    camera=driver.find_element(By.XPATH,'(//i[@class="K1-icon-right K1-icon-sm"])[4]')
    a.move_to_element(camera).perform()
    time.sleep(3)
    driver.find_element(By.XPATH,'//a[@id="vlogcamera"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH,'//button[@class="small-button icon-only sf-button"][1]').click()
    time.sleep(5)

login()
product()