"""
File should contain helper functions for the API.
For example use mock API calls to get data for the tests.
"""
import logging

logger = logging.getLogger("sauceDemo")


class APIHelper:
    """
    Mock API helper class to get data from the API.
    """
    @staticmethod
    def get_image_src() -> dict:
        """
        Mock API call to get image id by product name from the API
        :return: Image sources
        :rtype: dict
        """
        logger.info("Getting image sources from the API")
        path = "/static/media/"
        images = {
            "Sauce Labs Onesie": f"{path}red-onesie-1200x1500.2ec615b2.jpg",
            "Sauce Labs Bike Light": f"{path}bike-light-1200x1500.37c843b0.jpg",
            "Sauce Labs Bolt T-Shirt": f"{path}bolt-shirt-1200x1500.c2599ac5.jpg",
            "Test.allTheThings() T-Shirt (Red)": f"{path}red-tatt-1200x1500.30dadef4.jpg",
            "Sauce Labs Backpack": f"{path}sauce-backpack-1200x1500.0a0b85a3.jpg",
            "Sauce Labs Fleece Jacket": f"{path}sauce-pullover-1200x1500.51d7ffaf.jpg"
        }
        return images
