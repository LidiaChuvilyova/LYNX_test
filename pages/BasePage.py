from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.browser.get(self.url)

    def open(self):
        self.browser.get(self.url)

    def wait_and_find_element(self, how, what, timeout=10):
        element = WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what)))
        return element

    def is_element_present(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False
        return True

    def get_text_input(self, how, what):
        inputText = self.browser.find_element(how, what)
        return inputText

    def set_text_input(self, how, what, value):
        inputText = self.get_text_input(how, what)
        inputText.send_keys(value)
        print(f"Input text {value}")

    def select_by_value(self, how, what, value):
        selectItem = self.browser.find_element(how, what)
        Select(selectItem).select_by_value(value)
        print(f"Select option {value}")
