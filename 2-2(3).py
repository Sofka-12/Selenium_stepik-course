from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    browser.find_element(By.NAME, "email").send_keys("test@test.com")

    file_name = "file.txt"
    file_path = os.path.abspath(file_name)

    with open(file_path, "w") as file:
        file.write("")

    browser.find_element(By.ID, "file").send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(30)
    browser.quit()
    