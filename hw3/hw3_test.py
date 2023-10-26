from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
from data import URL_TEST, LOGIN, PASSWORD

#Перейти по URL: Открыть в браузере указанный URL сайта https://victoretc.github.io/selenium_waits/
def test_get_url(driver):
    driver.get(URL_TEST)

    assert driver.current_url == 'https://victoretc.github.io/selenium_waits/'

# Проверить заголовок: Убедиться, что текст в теге <h1> на странице соответствует "Практика с ожиданиями в Selenium".
def test_text_h1(driver):
    driver.get(URL_TEST)
    test_tag = driver.find_element(By.CSS_SELECTOR, 'h1')

    assert test_tag.text == "Практика с ожиданиями в Selenium"

# Дождаться появления кнопки "Начать тестирование"
# Найти кнопку: Найти на странице кнопку с текстом "Начать тестирование".
# Начать тестирование: Кликнуть по кнопке "Начать тестирование".
def test_button_start(driver,wait):
    driver.get(URL_TEST)

    button_start_test = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='startTest']")))
    # button_start_test = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='startTest']")))
    driver.find_element(By.XPATH,"//*[@id='startTest']" ).click()

    assert 'Начать тестирование' in button_start_test.text

# Ввод логина: Ввести "login" в поле для логина.
# Ввод пароля: Ввести "password" в поле для пароля.
# Согласие с правилами: Установить флажок в чекбокс "Согласен со всеми правилами".
# Подтвердить регистрацию: Нажать кнопку "Зарегистрироваться".
# Проверка загрузки: Удостовериться, что появился индикатор загрузки.
def test_login(driver,wait):
    driver.get(URL_TEST)

    button_start_test = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='startTest']"))).click()
    driver.find_element(By.XPATH, "// *[ @ id = 'login']").send_keys(LOGIN)
    driver.find_element(By.XPATH, "// *[ @ id = 'password']").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//*[@type='checkbox']").click()
    driver.find_element(By.XPATH, "//*[@id='register']").click()

    loader = driver.find_element(By.XPATH, "//*[@id='loader']")

    assert loader.is_displayed()
    assert 'Загрузка...' in loader.text

# Проверка сообщения: Убедиться, что после завершения загрузки появилось сообщение "Вы успешно зарегистрированы".
def test_final(driver,wait):
    driver.get(URL_TEST)

    button_start_test = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='startTest']"))).click()
    driver.find_element(By.XPATH, "// *[ @ id = 'login']").send_keys(LOGIN)
    driver.find_element(By.XPATH, "// *[ @ id = 'password']").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//*[@type='checkbox']").click()
    driver.find_element(By.XPATH, "//*[@id='register']").click()

    final = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id ='successMessage']")))

    assert "Вы успешно зарегистрированы!" in final.text
