import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
    