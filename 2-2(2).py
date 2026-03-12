from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://SunInJuly.github.io/execute_script.html")

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    browser.execute_script("arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    radiobutton = browser.find_element(By.ID, "robotsRule")

    browser.execute_script("arguments[0].click();", checkbox)
    browser.execute_script("arguments[0].click();", radiobutton)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("arguments[0].click();", button)

finally:
    time.sleep(30)
    browser.quit()
    