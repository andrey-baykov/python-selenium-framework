from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebDriverExtended:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def navigate_to(self, url: str):
        """
        Method to navigate to a URL.
        :param str url: The URL to navigate to.
        """
        self.driver.get(url)

    def wait_for_element(self, locator: tuple[str, str], timeout: int = 10) -> WebElement:
        """
        Wait for an element to become visible and return it.
        :param tuple[str, str] locator: The locator of the element.
        :param int timeout: The timeout in seconds.
        :return: The element.
        :rtype: WebElement
        """
        element_present = EC.visibility_of_element_located(locator)
        return WebDriverWait(self.driver, timeout).until(element_present)

    def click_element(self, locator: tuple[str, str] | WebElement):
        """
        Wait for an element and click it.
        :param tuple[str, str] | WebElement locator: The locator of the element or WebElement.
        """
        if type(locator) is WebElement:
            element = locator
        else:
            element = self.wait_for_element(locator)
        element.click()

    def type_text(self, locator: tuple[str, str], text: str):
        """
        Wait for an element and type text into it.
        :param tuple[str, str] locator: The locator of the element.
        :param str text: The text to type.
        """
        element = self.wait_for_element(locator)
        element.send_keys(text)

    def get_title(self) -> str:
        """
        Method to get the title of the page.
        :return: The title of the page.
        :rtype: str
        """
        return self.driver.title

    def get_elements(self, locator: tuple[str, str]) -> list:
        """
        Method to get a list of elements.
        :param tuple[str, str] locator: The locator of the elements.
        :return: The list of elements.
        :rtype: list
        """
        return self.driver.find_elements(*locator)

    def get_element(self, locator: tuple[str, str]) -> WebElement:
        """
        Method to get an element.
        :param tuple[str, str] locator: The locator of the element.
        :return: The element.
        :rtype: WebElement
        """
        return self.driver.find_element(*locator)
