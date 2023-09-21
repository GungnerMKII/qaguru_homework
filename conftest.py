import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def setting_browser():
    browser.config.window_width = 920
    browser.config.window_height = 860
    yield
    browser.quit() 
    
@pytest.fixture(scope="function")
def open_google():
    browser.open('https://google.com')
    
@pytest.fixture(scope='function')
def open_demoqa_textbox():
    browser.open('https://demoqa.com/text-box')