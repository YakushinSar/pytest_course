import pytest
from selenium import webdriver
from locators import USERNAME_FIELD, PASSWORD_FIELD,LOGIN_BUTTON,CART_BUTTON,BORGER_BUTTON
from data import URL_TEST, USERNAME, PASSWORD, PASSWORD_NOT_CORRECT, FIRST_NAME, LAST_NAME, ZIP_CODE,URL_PAGE
from selenium.webdriver.common.by import By

@pytest.fixture()
def driver():
    #создание драйвера
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture()
def authorization(driver):
    #авторизация с коректными данными
    driver.get(URL_TEST)
    driver.maximize_window()
    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(USERNAME)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(By.XPATH, LOGIN_BUTTON).click()
    yield driver
    driver.quit()

# Образец
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://selenium1py.pythonanywhere.com/"
#
# @pytest.fixture
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     # этот код выполнится после завершения теста
#     print("\nquit browser..")
#     browser.quit()
#
#
# class TestMainPage1():
#     # вызываем фикстуру в тесте, передав ее как параметр
#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")