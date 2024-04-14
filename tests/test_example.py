import allure
import pytest
from helpers.logger_helper import setup_logging
from helpers.api_helper import APIHelper
from pages.cart import CartPage, CartPageLocators
from pages.checkout import CheckoutPage, CheckoutPageLocators
from pages.login import LoginPage
from pages.products import ProductsPage, ProductsPageLocators
from tests.common import TestCommon

logger = setup_logging()
logger.info("Application started")


@allure.suite("Test assignment for SauceDemo.com")
@pytest.mark.usefixtures("driver_setup", "base_url")
class TestCases(TestCommon):
    """
    Test class to test following scenarios:
    - Standard user can complete purchase
    - Locked out user cannot login
    - Problem user encounters issues
    """
    @allure.title("Standard User Checkout Test")
    @pytest.mark.parametrize("credentials", ["standard"], indirect=True)
    def test_standard_user_can_complete_purchase(self, driver_setup, credentials, base_url):
        """
        Tests that a standard user can log in, add items, and complete a purchase.
        Validates all key steps and actions.
        :param driver_setup: Fixture to set up the driver.
        :param credentials: Fixture to return the credentials for a 'standard' user.
        :param base_url: Fixture to return the base URL.
        """
        logger.info("Starting test_standard_user_can_complete_purchase")
        with allure.step("Initialize the WebDriver"):
            driver = driver_setup
            logger.info("WebDriver initialized successfully")

        with allure.step("Login as a standard user"):
            login_page = LoginPage(driver)
            self.login_user(login_page, credentials, base_url)
            logger.info("User logged in successfully")

        with allure.step("Verify product page is loaded"):
            product_page = ProductsPage(driver)
            product_page.verify_page()
            logger.info("Product page loaded successfully")

        with allure.step("Verify sorting options AZ"):
            self.verify_sorting_options(product_page, "az")

        with allure.step("Verify sorting options ZA"):
            self.verify_sorting_options(product_page, "za")

        with allure.step("Verify sorting options LOHI"):
            self.verify_sorting_options(product_page, "lohi")

        with allure.step("Verify sorting options HILO"):
            self.verify_sorting_options(product_page, "hilo")

        with allure.step("Verify add 3 items to cart"):
            logger.info("Adding 3 items to cart")
            product_names = product_page.get_elements(ProductsPageLocators.product_name)[0:3]
            product_buttons = product_page.get_elements(ProductsPageLocators.button_add_to_cart)
            for i in range(3):
                product_page.click_element(product_buttons[i])
                assert product_page.get_element(ProductsPageLocators.shopping_cart_badge).text == str(i + 1), "Item not added to cart!"
                logger.info(f"Item {i + 1} added to cart")
                assert product_page.get_element(ProductsPageLocators.shopping_cart_badge).is_displayed(), "Cart badge not displayed!"
                logger.info("Cart badge displayed")

        with allure.step("Verify cart has 3 items"):
            product_page.click_element(ProductsPageLocators.button_cart)
            cart_page = CartPage(driver)
            cart_page.verify_page()
            cart_page.verify_cart_items(product_names)
            logger.info("Cart has 3 items")

        with allure.step("Verify checkout Information page"):
            cart_page.click_element(CartPageLocators.button_checkout)
            checkout_page = CheckoutPage(driver)
            checkout_page.verify_page("Checkout: Your Information")
            checkout_page.fill_checkout_data()

        with allure.step("Verify checkout Overview page"):
            checkout_page.verify_page("Checkout: Overview")
            checkout_page.verify_data_checkout_overview()
            checkout_page.click_element(CheckoutPageLocators.button_finish)
            logger.info("Checkout completed")

        with allure.step("Verify checkout Complete page"):
            checkout_page.verify_page("Checkout: Complete!")
            assert checkout_page.get_elements(ProductsPageLocators.shopping_cart_badge) == [], "Items still added to cart!"
            checkout_page.click_element(CheckoutPageLocators.button_home)
            logger.info("Checkout complete page verified")

        with allure.step("Verify logout"):
            product_page.verify_page()
            product_page.click_element(ProductsPageLocators.button_menu)
            product_page.click_element(ProductsPageLocators.button_logout)
            assert login_page.get_title() == "Swag Labs", "Title should be 'Swag Labs'"
            logger.info("User logged out successfully")

    @allure.title("Locked Out User Login Test")
    @pytest.mark.parametrize("credentials", ["locked_out"], indirect=True)
    def test_locked_out_user_cannot_login(self, driver_setup, credentials, base_url):
        """
        Verifies that a locked out user cannot log in and receives the correct error message.
        :param driver_setup: Fixture to set up the driver.
        :param credentials: Fixture to return the credentials for a 'locked_out' user.
        :param base_url: Fixture to return the base URL.
        """
        logger.info("Starting test_locked_out_user_cannot_login")
        with allure.step("Initialize the WebDriver"):
            driver = driver_setup
            logger.info("WebDriver initialized successfully")

        with allure.step("Login as a locked out user"):
            login_page = LoginPage(driver)
            self.login_user(login_page, credentials, base_url)
            assert login_page.get_error_message() == "Epic sadface: Sorry, this user has been locked out.", "User should be locked out."
            logger.info("User locked out successfully")

    @allure.title("Problem User Test")
    @pytest.mark.parametrize("credentials", ["problem"], indirect=True)
    def test_problem_user_encounters_issues(self, driver_setup, credentials, base_url):
        """
        Ensures that a problem user encounters expected issues during login.
        :param driver_setup: Fixture to set up the driver.
        :param credentials: Fixture to return the credentials for a 'problem' user.
        :param base_url: Fixture to return the base URL.
        """
        logger.info("Starting test_problem_user_encounters_issues")
        with allure.step("Initialize the WebDriver"):
            driver = driver_setup
            logger.info("WebDriver initialized successfully")

        with allure.step("Login as a problem user"):
            login_page = LoginPage(driver)
            self.login_user(login_page, credentials, base_url)
            logger.info("User logged in successfully")

        with allure.step("Verify product page is loaded"):
            product_page = ProductsPage(driver)
            product_page.verify_page()

        with allure.step("Verify image validation"):
            product_page.verify_image_src(APIHelper.get_image_src())
            logger.info("Image validation successful")

        with allure.step("Verify user information page"):
            # User information is not present in web app, so this step is skipped
            assert True, "User information not present in web app."
            logger.debug("User information page not validated")
