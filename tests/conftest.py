import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def setting_browser():
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument("--headless=new")
    browser.config.driver_options = driver_options
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_height = 1000
    browser.config.window_width = 900
    yield
    browser.quit()
