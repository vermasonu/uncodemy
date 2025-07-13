from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
driver.maximize_window()
time.sleep(2)
f=driver.find_element(By.XPATH,'//iframe[@class="demo-frame lazyloaded"]')
driver.switch_to.frame(f)
time.sleep(2)
a=ActionChains(driver)
src=driver.find_element(By.XPATH,"//img[@alt='The peaks of High Tatras']")
dest=driver.find_element(By.XPATH,"//div[@id='trash']")
a.drag_and_drop(src,dest).perform()
src1=driver.find_element(By.XPATH,"//img[@alt='The chalet at the Green mountain lake']")
a.drag_and_drop(src1,dest).perform()
src2=driver.find_element(By.XPATH,"//img[@alt='Planning the ascent']")
a.drag_and_drop(src2,dest).perform()
src3=driver.find_element(By.XPATH,"//img[@alt='On top of Kozi kopka']")
a.drag_and_drop(src3, dest).perform()
time.sleep(5)