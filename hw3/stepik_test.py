from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def test_stepik():
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait1.html")

    button = browser.find_element(By.ID, "verify").click()

    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

def test_stepik_time():
    #time
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait1.html")

    time.sleep(1)
    button = browser.find_element(By.ID, "verify").click()

    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

def   test_stepik_implicit():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/wait1.html")

    button = browser.find_element(By.ID, "verify").click()

    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

def test_stepik_explicit():
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))
    # проверка что кнопка  неактивна
    # button = WebDriverWait(browser, 5).until_not(EC.element_to_be_clickable((By.ID, "verify")))
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text