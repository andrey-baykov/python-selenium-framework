import logging
from helpers.webdriver_helper import WebDriverExtended
from selenium.webdriver.common.by import By

logger = logging.getLogger("sauceDemo")


class BasePageLocators:
    app_logo = (By.XPATH, "//div[@class='app_logo']")
    page_title = (By.XPATH, "//span[@data-test='title']")
    button_cart = (By.XPATH, "//a[@class='shopping_cart_link']")
    shopping_cart_badge = (By.XPATH, "//span[@class='shopping_cart_badge']")

    button_menu = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    button_all_items = (By.XPATH, "//a[text()='All Items']")
    button_about = (By.XPATH, "//a[text()='About']")
    button_logout = (By.XPATH, "//a[text()='Logout']")
    button_reset_app_state = (By.XPATH, "//a[text()='RESET APP STATE']")

    product_name = (By.XPATH, "//div[@data-test='inventory-item-name']")
    product_price = (By.XPATH, "//div[@data-test='inventory-item-price']")
    product_description = (By.XPATH, "//div[@data-test='inventory_item-desc']")
    product_image_src = (By.XPATH, f"//div[@data-test='inventory-item']//img")

    button_add_to_cart = (By.XPATH, "//button[text()='Add to cart']")
    button_remove_from_cart = (By.XPATH, "//button[text()='Remove']")


class BasePage(WebDriverExtended):
    """
    This class contains the base page object.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self, url):
        """
        Method to open the page.
        """
        logger.info(f"Opening the page: {url}")
        self.navigate_to(url)
