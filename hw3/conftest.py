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

# @pytest.fixture
# #с неявным ожиданием
# def driver(chrome_options):
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()

@pytest.fixture
#с явным ожиданием
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait

@pytest.fixture
def login(driver):
    driver.get(URL_TEST)
    driver.find_element(By.XPATH, "//*[@id='startTest']").click()
    driver.find_element(By.XPATH, "// *[ @ id = 'login']").send_keys(LOGIN)
    driver.find_element(By.XPATH, "// *[ @ id = 'password']").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//*[@type='checkbox']").click()
    driver.find_element(By.XPATH, "//*[@id='register']").click()



