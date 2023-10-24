import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(scope="function", autouse=True)
def setting_browser():
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless=new')
    browser.config.driver_options = driver_options
    browser.config.window_width = 1080
    browser.config.window_height = 860
    yield
    browser.quit() 