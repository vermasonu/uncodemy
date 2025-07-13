from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
driver= webdriver.Chrome()
driver.get("https://www.automationexercise.com/")
driver.maximize_window()
# time.sleep(3)
a=ActionChains(driver)
def login():

    login=driver.find_element(By.XPATH,"//a[normalize-space()='Signup / Login']").click()
    driver.find_element(By.XPATH,"//input[@data-qa='login-email']").send_keys("sonuverma2505@gmail.com")
    driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("Navanya@321")
    driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
    time.sleep(3)
def product():
    # a = ActionChains(driver)
    # prod=driver.find_element(By.XPATH,'(//i[@class="K1-icon-down K1-icon-sm"])[1]')
    # a.move_to_element(prod).perform()
    # time.sleep(3)
    # camera=driver.find_element(By.XPATH,'(//i[@class="K1-icon-right K1-icon-sm"])[4]')
    # a.move_to_element(camera).perform()
    # time.sleep(3)
    # driver.find_element(By.XPATH,'//a[@id="vlogcamera"]').click()
    # time.sleep(3)
    driver.find_element(By.XPATH,"//a[@href='/products']").click()
    time.sleep(2)
    c1=driver.find_element(By.XPATH,'//img[@src="/get_product_picture/5"]')
    actions=ActionChains(driver)
    actions.move_to_element(c1).perform()
    time.sleep(2)
    driver.find_element(By.XPATH, '(//a[@data-product-id="5"])[2]').click()
    time.sleep(3)
    c=driver.find_element(By.XPATH,'//div[@class="modal-content"]')
    actions.move_to_element(c).perform()
    driver.find_element(By.XPATH,'//button[@class="btn btn-success close-modal btn-block"]').click()
    time.sleep(2)

def cart():
    cart=driver.find_element(By.XPATH,'/html[1]/body[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]')
    a.move_to_element(cart).perform()
    cart.click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[@class='btn btn-default check_out']").click()
    time.sleep(2)
    order=driver.find_element(By.XPATH,"//a[@class='btn btn-default check_out']")
    a.move_to_element(order).perform()
    order.click()

def card():
    driver.find_element(By.XPATH,"//input[@name='name_on_card']").send_keys("test")
    driver.find_element(By.XPATH,"//input[@name='card_number']").send_keys("111122223333")
    driver.find_element(By.XPATH,"//input[@placeholder='ex. 311']").send_keys("321")
    driver.find_element(By.XPATH,"//input[@placeholder='MM']").send_keys("25")
    driver.find_element(By.XPATH,"//input[@placeholder='YYYY']").send_keys("2030")
    driver.find_element(By.XPATH,"//button[@id='submit']").click()
    time.sleep(3)
login()
product()
cart()
card()