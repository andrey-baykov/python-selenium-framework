"""
Class for common test functions
"""
from pages.products import ProductsPageLocators
import logging

logger = logging.getLogger("sauceDemo")


class TestCommon:
    @staticmethod
    def login_user(login_page, credentials, url: str):
        """
        Helper method to log in a user.
        :param login_page: The login page object.
        :param credentials: The credentials to use to log in.
        :param str url: URL to open.
        """
        login_page.open(url)
        try:
            assert login_page.get_title() == "Swag Labs", "Title should be 'Swag Labs'"
            logger.info("Login page opened successfully with title 'Swag Labs")
        except AssertionError:
            logger.error("Login page not opened successfully with title 'Swag Labs'")
        username, password = credentials
        login_page.input_user_name(username)
        login_page.input_password(password)
        login_page.button_click()

    def verify_sorting_options(self, product_page, sort_option: str):
        """
        Helper method to verify the sorting options on the product page.
        :param product_page: The product page object.
        :param str sort_option: The sorting option to verify.
        """
        product_page.click_element(ProductsPageLocators.sort_dropdown)
        product_page.click_element(getattr(ProductsPageLocators, f"sort_dropdown_option_{sort_option}"))
        product_names = product_page.get_elements(ProductsPageLocators.product_name)
        product_prices = product_page.get_elements(ProductsPageLocators.product_price)
        try:
            if sort_option in ["az", "za"]:
                assert self.verify_sorted(product_names, sort_option), "Product names are not sorted correctly!"
                logger.info(f"Product names are sorted correctly in {sort_option} order")
            else:
                assert self.verify_sorted(product_prices, sort_option), "Product prices are not sorted correctly!"
                logger.info(f"Product prices are sorted correctly in {sort_option} order")
        except AssertionError as e:
            logger.error(f"Product names/prices are not sorted correctly in {sort_option} order")
            logger.error(e)

    @staticmethod
    def verify_sorted(elements, order: str) -> bool:
        """
        Helper method to verify if a list of elements is sorted.
        :param elements: The list of elements to verify.
        :param str order: The order to verify the elements in.
        :return: True if the elements are sorted, False otherwise.
        :rtype: bool
        """
        logger.info(f"Verifying if elements are sorted in {order} order")
        if order == "az":
            return elements == sorted(elements, key=lambda x: str(x.text[1:]))
        elif order == "za":
            return elements == sorted(elements, key=lambda x: str(x.text[1:]), reverse=True)
        elif order == "lohi":
            return elements == sorted(elements, key=lambda x: float(x.text[1:]))
        elif order == "hilo":
            return elements == sorted(elements, key=lambda x: float(x.text[1:]), reverse=True)
        else:
            logger.error("Invalid order")
            return False

    @staticmethod
    def get_buttons_list(product_page) -> list:
        """
        Helper method to get the list of add to cart buttons.
        :param product_page: The product page object.
        :return: The list of 'add to cart' buttons.
        :rtype: list
        """
        logger.info("Getting the list of 'add to cart' buttons")
        return product_page.get_elements(product_page.button_add_to_cart)
