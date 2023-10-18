import pytest
from selenium import webdriver
from locators import USERNAME_FIELD, PASSWORD_FIELD,LOGIN_BUTTON,CART_BUTTON,BORGER_BUTTON
from data import URL_TEST, USERNAME, PASSWORD, PASSWORD_NOT_CORRECT, FIRST_NAME, LAST_NAME, ZIP_CODE,URL_PAGE
from selenium.webdriver.common.by import By

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    print('\nquit browser...')
    driver.quit()

@pytest.fixture()
def authorization():
    driver = webdriver.Chrome()
    driver.get(URL_TEST)
    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(USERNAME)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(By.XPATH, LOGIN_BUTTON).click()
    yield driver
    print('\nquit browser...')
    driver.quit()

