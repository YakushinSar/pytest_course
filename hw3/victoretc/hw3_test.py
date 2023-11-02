# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import pytest
import time

from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import URL_TEST, LOGIN, PASSWORD
from locators import LOGIN_FIELD, PASSWORD_FIELD, CHECXBOX, REGISTER_BUTTON, FINAL_MASSAGE, BUTTON_START_TEST


# Перейти по URL: Открыть в браузере указанный URL сайта https://victoretc.github.io/selenium_waits/
# Проверить заголовок: Убедиться, что текст в теге <h1> на странице соответствует "Практика с ожиданиями в Selenium".
# Дождаться появления кнопки "Начать тестирование"
# Найти кнопку: Найти на странице кнопку с текстом "Начать тестирование".
# Начать тестирование: Кликнуть по кнопке "Начать тестирование".
# Ввод логина: Ввести "login" в поле для логина.
# Ввод пароля: Ввести "password" в поле для пароля.
# Согласие с правилами: Установить флажок в чекбокс "Согласен со всеми правилами".
# Подтвердить регистрацию: Нажать кнопку "Зарегистрироваться".
# Проверка загрузки: Удостовериться, что появился индикатор загрузки.
# Проверка сообщения: Убедиться, что после завершения загрузки появилось сообщение "Вы успешно зарегистрированы".

# Ожидаемый результат:** Пользователь успешно проходит процесс регистрации, видит индикатор загрузки и получает сообщение об успешной регистрации.
# Критерии успешности:** Сообщение "Вы успешно зарегистрированы" отображается на экране.

# Важно!
# Необходимо написать 3 автотеста для данной страницы
# 1. С использованием time.sleep()
# 2. С использованием Implicit waits
# 3. С использованием Explicit waits

def test_time(driver):
    driver.get(URL_TEST)
    assert driver.current_url == 'https://victoretc.github.io/selenium_waits/'

    test_tag = driver.find_element(By.CSS_SELECTOR, 'h1')
    time.sleep(7)
    assert test_tag.text == "Практика с ожиданиями в Selenium"

    button_start_test = driver.find_element(By.XPATH, "//*[@id='startTest']")
    assert 'Начать тестирование' in button_start_test.text
    button_start_test.click()

    driver.find_element(By.XPATH, LOGIN_FIELD).send_keys(LOGIN)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(By.XPATH, CHECXBOX).click()
    driver.find_element(By.XPATH, REGISTER_BUTTON).click()
    time.sleep(2)

    loader = driver.find_element(By.XPATH, "//*[@id='loader']")
    assert loader.is_displayed() == True
    assert loader.text == 'Загрузка...'
    time.sleep(5)

    final = driver.find_element(By.XPATH, FINAL_MASSAGE)
    assert final.text == "Вы успешно зарегистрированы!", 'Регистрация не прошла'


def test_impl(driver1):
    driver1.get(URL_TEST)
    assert driver1.current_url == 'https://victoretc.github.io/selenium_waits/'

    test_tag = driver1.find_element(By.CSS_SELECTOR, 'h1')

    assert test_tag.text == "Практика с ожиданиями в Selenium"
    # time.sleep(6)
    button_start_test = driver1.find_element(By.XPATH, BUTTON_START_TEST)
    # assert button_start_test.text == ' Начать тестирование '
    button_start_test.click()

    driver1.find_element(By.XPATH, LOGIN_FIELD).send_keys(LOGIN)
    driver1.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)
    driver1.find_element(By.XPATH, CHECXBOX).click()
    driver1.find_element(By.XPATH, REGISTER_BUTTON).click()

    loader = driver1.find_element(By.XPATH, "//*[@id='loader']")
    assert loader.is_displayed() == True
    assert loader.text == 'Загрузка...'

    final = driver1.find_element(By.XPATH, FINAL_MASSAGE)
    assert final.is_displayed() == True
    assert final.text == "Вы успешно зарегистрированы!", 'Регистрация не прошла'


def test_expl(driver, wait):
    driver.get(URL_TEST)
    assert driver.current_url == 'https://victoretc.github.io/selenium_waits/'

    test_tag = driver.find_element(By.CSS_SELECTOR, 'h1')

    assert test_tag.text == "Практика с ожиданиями в Selenium"

    button_start_test = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='startTest']")))
    # button_start_test = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='startTest']")))
    assert 'Начать тестирование' in button_start_test.text
    button_start_test.click()

    driver.find_element(By.XPATH, LOGIN_FIELD).send_keys(LOGIN)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(By.XPATH, CHECXBOX).click()
    driver.find_element(By.XPATH, REGISTER_BUTTON).click()

    loader = driver.find_element(By.XPATH, "//*[@id='loader']")
    assert loader.is_displayed() == True
    assert loader.text == 'Загрузка...'

    final = wait.until(EC.element_to_be_clickable((By.XPATH, FINAL_MASSAGE)))
    assert final.text == "Вы успешно зарегистрированы!", 'Регистрация не прошла'
    print(final.text)
