from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

button = browser.find_element(By.TAG_NAME, "button")
button.click()

alert = browser.switch_to.alert
alert.accept()

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
answer = calc(x)

input_field = browser.find_element(By.ID, "answer")
input_field.send_keys(answer)

submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit_button.click()

time.sleep(5)

browser.quit()
