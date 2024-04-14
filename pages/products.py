import logging
from selenium.webdriver.common.by import By
from pages.base import BasePage, BasePageLocators
from urllib.parse import urlparse

logger = logging.getLogger("sauceDemo")


class ProductsPageLocators(BasePageLocators):
    """
    Specific locators for the products page.
    """
    sort_dropdown = (By.XPATH, "//select[@class='product_sort_container']")
    sort_dropdown_option_az = (By.XPATH, "//option[@value='az']")
    sort_dropdown_option_za = (By.XPATH, "//option[@value='za']")
    sort_dropdown_option_lohi = (By.XPATH, "//option[@value='lohi']")
    sort_dropdown_option_hilo = (By.XPATH, "//option[@value='hilo']")


class ProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_page(self):
        """
        Method to verify the products page.
        """
        # Can be moved to a BasePage, still here for demonstration purposes
        logger.info("Verifying the products page")
        assert self.wait_for_element(ProductsPageLocators.page_title).text == "Products", "Products page not loaded!"

    def verify_image_src(self, image_src_expected: dict):
        """
        Method to verify the image source.
        :param dict image_src_expected: The expected image source.
        """
        logger.info("Verifying image source")
        image_src_actual = self.get_elements(ProductsPageLocators.product_image_src)
        product_actual = self.get_elements(ProductsPageLocators.product_name)
        result = []
        for i in range(len(image_src_actual)):
            full_src = image_src_actual[i].get_attribute("src")
            parsed_url = urlparse(full_src)
            src_actual = f"{parsed_url.path}"
            src_expected = image_src_expected[product_actual[i].text]
            if src_actual == src_expected:
                logger.info(f"Image source actual '{src_actual}' as expected '{src_expected}'")
                result.append(True)
            else:
                logger.error(f"Image source actual '{src_actual}' not as expected '{src_expected}'")
                result.append(False)

        assert all(result), "Not all image sources are as expected!"