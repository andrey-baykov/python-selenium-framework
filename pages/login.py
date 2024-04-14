"""
This module contains the page object for the login page.
"""

from selenium.webdriver.common.by import By
from pages.base import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPageLocators:
    """
    Locators for the login page.
    """
    input_login = (By.XPATH, "//input[@id='user-name']")
    input_password = (By.XPATH, "//input[@id='password']")
    button_login = (By.XPATH, "//input[@id='login-button']")
    error_message = (By.XPATH, "//h3[@data-test='error']")


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def input_user_name(self, username: str):
        """
        Method to input the username.
        :param str username: Username to input.
        """
        self.type_text(LoginPageLocators.input_login, username)

    def input_password(self, password: str):
        """
        Method to input the password.
        :param str password: Password to input.
        """
        self.type_text(LoginPageLocators.input_password, password)

    def button_click(self):
        """
        Method to click the login button.
        """
        self.click_element(LoginPageLocators.button_login)

    def get_error_message(self):
        """
        Method to get the error message text on login page.
        """
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LoginPageLocators.error_message),
                                                       message="Error message not found!")
        return element.text
