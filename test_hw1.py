from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# 1.Авторизация
#-Авторизация с использованием корректных данных (standard_user, secret_sauce)

def test_avtorization_correct():
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    username = driver.find_element(By.XPATH,"//*[@placeholder='Username']")
    username.send_keys('standard_user')

    password = driver.find_element(By.XPATH, "//*[@placeholder='Password']")
    password.send_keys('secret_sauce')

    button_login = driver.find_element(By.XPATH, "//*[@data-test='login-button']")
    button_login.click()

    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'
    print(driver.current_url)

    driver.quit()


#-Авторизация с использованием некорректированных данных (пользователя, пользователя)
def test_avtorization_not_correct():
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    username = driver.find_element(By.XPATH, "//*[@placeholder='Username']")
    username.send_keys('standard')

    password = driver.find_element(By.XPATH, "//*[@placeholder='Password']")
    password.send_keys('secret')

    button_login = driver.find_element(By.XPATH, "//*[@data-test='login-button']")
    button_login.click()

    button_error  = driver.find_element(By.XPATH, "//*[@data-test='error']")
    assert button_error.text == 'Epic sadface: Username and password do not match any user in this service'
    print(button_error.text)

    driver.quit()


# 2.Корзина
#-Добавление товара в корзину через каталог
def test_adding_to_cart():
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    username = driver.find_element(By.XPATH,"//*[@placeholder='Username']")
    username.send_keys('standard_user')

    password = driver.find_element(By.XPATH, "//*[@placeholder='Password']")
    password.send_keys('secret_sauce')

    button_login = driver.find_element(By.XPATH, "//*[@data-test='login-button']")
    button_login.click()

    adding_to_cart = driver.find_element(By.XPATH, "//*[@data-test='add-to-cart-sauce-labs-backpack']")
    adding_to_cart.click()

    button_remove = driver.find_element(By.XPATH, "//*[@data-test='remove-sauce-labs-backpack']")

    assert button_remove.text == 'Remove'
    print(button_remove.text)

    driver.quit()


#-Удаление товара из корзины через карточку товара
def test_delete_card():
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    username = driver.find_element(By.XPATH, "//*[@placeholder='Username']")
    username.send_keys('standard_user')

    password = driver.find_element(By.XPATH, "//*[@placeholder='Password']")
    password.send_keys('secret_sauce')

    button_login = driver.find_element(By.XPATH, "//*[@data-test='login-button']")
    button_login.click()

    adding_to_cart = driver.find_element(By.XPATH, "//*[@data-test='add-to-cart-sauce-labs-backpack']")
    adding_to_cart.click()

    button_remove = driver.find_element(By.XPATH, "//*[@data-test='remove-sauce-labs-backpack']")
    button_remove.click()

    adding_to_cart_after_delete = driver.find_element(By.XPATH, "//*[@data-test='add-to-cart-sauce-labs-backpack']")
    assert adding_to_cart_after_delete.text == 'Add to cart', 'Данный тест упал'
    print(adding_to_cart_after_delete.text)

    driver.quit()

#-Удаление товара из корзины через корзину