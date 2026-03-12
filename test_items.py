from selenium.webdriver.common.by import By
import time


def test_guest_should_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    time.sleep(30)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")

    assert button is not None
    