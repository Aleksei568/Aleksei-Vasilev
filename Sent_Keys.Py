from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
try:
    driver.get('http://www.lambdatest.com/selenium-playground/simple-form-demo')
    sleep(2)
    driver.maximize_window()
    input_field = driver.find_element(By.ID, "user-message")
    sleep(2)
    input_field.send_keys('текст пользователя')
    sleep(2)
    button = driver.find_element(By.ID, "showInput")
    sleep(2)
    button.click()
    sleep(3)
finally:
    driver.quit()
