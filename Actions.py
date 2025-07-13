from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://uncodemy.com/")
time.sleep(2)
driver.maximize_window()
actions=ActionChains(driver)
cat=driver.find_element(By.XPATH,'//span[@id="categoriesBtn"]')
actions.move_to_element(cat).perform()
time.sleep(5)
cat1=driver.find_element(By.XPATH,'(//menuitem[@class="SEt"])[3]')
actions.move_to_element(cat1).perform()
driver.find_element(By.XPATH,'(//menuitem[@label="Test 2"])[4]').click()
# driver.find_element(By.XPATH,'(//a[@href="/course/manual-testing-course-in-noida"][@class="has"])[1]').click()
# driver.find_element(By.XPATH,'//a[@href="/course/automation-testing-course-in-noida"][@class="has"]').click()
time.sleep(5)