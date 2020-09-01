"""Generic UI object for driving the POM."""
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait


class Browser:
    driver = None


class WebUIObject(Browser):
    def __init__(self, by: By, locator: str):
        super().__init__()
        self.by = by
        self.locator = locator
        self._wait = WebDriverWait(super().driver, 10)

    @property
    def _web_element(self):
        self._wait.until(expected.presence_of_element_located((self.by, self.locator)))
        return super().driver.find_element(self.by, self.locator)

    @property
    def text(self):
        return self._web_element.text

    def click(self):
        self._wait.until(expected.element_to_be_clickable((self.by, self.locator)))
        self._web_element.click()

    def type(self, text):
        self._web_element.send_keys(text)

    def is_visible(self):
        try:
            self._wait.until(expected.visibility_of_element_located((self.by, self.locator)))
            return True
        except TimeoutException:
            return False
