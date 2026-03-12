import unittest

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def register_user(link):
    with webdriver.Chrome() as browser:
        browser.get(link)

        browser.find_element('css selector', '.first_block .first').send_keys(
            'John'
        )
        browser.find_element('css selector', '.first_block .second').send_keys(
            'Doe'
        )
        browser.find_element('css selector', '.first_block .third').send_keys(
            'johndoe@gmail.com'
        )
        browser.find_element('tag name', 'button').click()

        welcome_text = (
            WebDriverWait(browser, 2)
            .until(ec.visibility_of_element_located(('tag name', 'h1')))
            .text
        )

    return welcome_text


class TestRegistration(unittest.TestCase):
    def test_successful_registration(self):
        welcome_text_expected = (
            'Congratulations! You have successfully registered!'
        )
        welcome_text_actual = register_user(
            'https://suninjuly.github.io/registration1.html'
        )

        self.assertEqual(
            welcome_text_actual,
            welcome_text_expected,
            f'Welcome text should be "{welcome_text_expected}", '
            f'but actual is "{welcome_text_actual}"',
        )

    def test_failed_registration(self):
        welcome_text_expected = (
            'Congratulations! You have successfully registered!'
        )
        welcome_text_actual = register_user(
            'https://suninjuly.github.io/registration2.html'
        )

        self.assertEqual(
            welcome_text_actual,
            welcome_text_expected,
            f'Welcome text should be "{welcome_text_expected}", '
            f'but actual is "{welcome_text_actual}"',
        )


if __name__ == '__main__':
    unittest.main()

    