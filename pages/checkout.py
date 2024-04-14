import logging
from selenium.webdriver.common.by import By
from pages.base import BasePage, BasePageLocators

logger = logging.getLogger('sauceDemo')


class CheckoutPageLocators(BasePageLocators):
    """
    Specific locators for the cart page.
    """
    first_name = (By.XPATH, "//input[@id='first-name']")
    last_name = (By.XPATH, "//input[@id='last-name']")
    postal_code = (By.XPATH, "//input[@id='postal-code']")
    button_continue = (By.XPATH, "//input[@value='Continue']")
    button_cancel = (By.XPATH, "//button[text()='Cancel']")
    button_finish = (By.XPATH, "//button[text()='Finish']")
    button_home = (By.XPATH, "//button[text()='Back Home']")
    error_message = (By.XPATH, "//h3[@data-test='error']")


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_page(self, page_title: str):
        """
        Method to verify the cart page.
        :param str page_title: The title of the page to verify.
        """
        # Can be moved to a BasePage, still here for demonstration purposes
        logger.info(f"Verifying {page_title} page")
        assert self.wait_for_element(CheckoutPageLocators.page_title).text == page_title, f"{page_title} page not loaded!"

    def fill_checkout_data(self):
        """
        Method to fill the checkout data.
        """
        logger.info("Filling checkout data")
        self.type_text(CheckoutPageLocators.first_name, "Name")
        self.type_text(CheckoutPageLocators.last_name, "Surname")
        self.type_text(CheckoutPageLocators.postal_code, "11111")
        self.click_element(CheckoutPageLocators.button_continue)

    @staticmethod
    def verify_data_checkout_overview():
        """
        Method to verify the checkout overview page
        """
        # Should be implemented verification of items, prices, taxes, total, etc.
        logger.debug("Verifying checkout overview page not implemented")
        assert True, "Checkout overview page not correct!"
