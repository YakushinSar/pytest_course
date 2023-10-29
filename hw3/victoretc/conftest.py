import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from data import URL_TEST, LOGIN, PASSWORD
@pytest.fixture
def chrome_options():
    options = Options()
    # options.add_argument('--window-size=200,200')
    options.add_argument('--headless')
    return options

@pytest.fixture
#с неявным ожиданием
def driver1(chrome_options):
    driver1 = webdriver.Chrome(options=chrome_options)
    driver1.implicitly_wait(10)
    yield driver1
    driver1.quit()

@pytest.fixture
#с явным,sleep ожиданием
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait





