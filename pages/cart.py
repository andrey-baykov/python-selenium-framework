from selenium.webdriver.common.by import By
from pages.base import BasePage, BasePageLocators


class CartPageLocators(BasePageLocators):
    """
    Specific locators for the cart page.
    """
    cart_item_quantity = (By.XPATH, "//div[@data-test='item-quantity']")
    button_continue_shopping = (By.XPATH, "//button[text()='Continue Shopping']")
    button_checkout = (By.XPATH, "//button[text()='Checkout']")


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_page(self):
        """
        Method to verify the cart page.
        """
        # Can be moved to a BasePage, still here for demonstration purposes
        assert self.wait_for_element(CartPageLocators.page_title).text == "Your Cart", "Cart page not loaded!"

    def verify_cart_items(self, items):
        """
        Method to verify the cart items.
        :param list[str] items: The list of items to verify.
        """
        # Not in requirements, but added for demonstration purposes
        # Can be improved to verify the quantity, names and prices of items as well
        cart_items = self.get_elements(CartPageLocators.cart_item_quantity)
        assert len(cart_items) == len(items), f"Quantity does not match!"
