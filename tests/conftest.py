import json
import pytest
import allure
import logging
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService


CONFIG_PATH = "data.json"


@pytest.fixture()
def config():
    """
    Fixture to return the configuration from the JSON file.
    """
    logger = logging.getLogger("sauceDemo")
    logger.info("Reading configuration from JSON file")
    try:
        with open(CONFIG_PATH) as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        path = "../" + CONFIG_PATH
        with open(path) as config_file:
            return json.load(config_file)


@pytest.fixture()
def driver_setup(request, config):
    """
    Fixture to return the driver instance based on the browser type and the base URL.
    :param request: Request object.
    :param config: Config object.
    :param logger: Logger object.
    """
    logger = logging.getLogger("sauceDemo")
    logger.info("Starting driver setup")
    browser = config.get('browser').lower()
    if browser == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    driver.maximize_window()
    before_failed = request.session.testsfailed
    yield driver
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name="Test failed", attachment_type=AttachmentType.PNG)
    driver.quit()


@pytest.fixture()
def credentials(request, config):
    """Fixture to return the credentials for a specific user."""
    # Credentials should be opened from a secure location and not stored in a JSON file.
    logger = logging.getLogger("sauceDemo")
    logger.info("Returning credentials for a specific user")
    return config[request.param]


@pytest.fixture()
def base_url(config):
    logger = logging.getLogger("sauceDemo")
    logger.info("Returning the base URL")
    return config["base_url"]
