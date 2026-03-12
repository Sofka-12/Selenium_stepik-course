from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price_condition = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = str(math.log(abs(12 * math.sin(int(x)))))

    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    alert = browser.switch_to.alert
    print(alert.text)

finally:
    browser.quit()

    