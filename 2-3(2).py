from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

browser.find_element(By.TAG_NAME, "button").click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x = browser.find_element(By.ID, "input_value").text
answer = calc(x)

browser.find_element(By.ID, "answer").send_keys(answer)
browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(5)
browser.quit()

