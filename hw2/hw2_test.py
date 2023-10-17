from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from locators import USERNAME_FIELD, PASSWORD_FIELD,LOGIN_BUTTON,CART_BUTTON
from data import URL_TEST, USERNAME, PASSWORD, PASSWORD_NOT_CORRECT

driver = webdriver.Chrome()

# 1.Авторизация
#-Авторизация с использованием корректных данных (standard_user, secret_sauce)
def test_avtorization_is_correct():
    driver.get(URL_TEST)
    driver.maximize_window()

    driver.find_element(By.XPATH,USERNAME_FIELD).send_keys(USERNAME)

    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'

#-Авторизация с использованием некорректированных данных (пользователя)
def test_avtorization_not_correct():
    driver.get(URL_TEST)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(USERNAME)

    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD_NOT_CORRECT)

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    text = driver.find_element(By.XPATH, "//*[@data-test='error']").text

    assert text == 'Epic sadface: Username and password do not match any user in this service'
    print(text)

# 2.Корзина
#-Добавление товара в корзину через каталог
def test_add_product_to_catalog():
    driver.get(URL_TEST)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(USERNAME)

    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    add_product_to_catalog = driver.find_element(By.XPATH, "//*[@data-test='add-to-cart-sauce-labs-backpack']").click()

    remove_button_text = driver.find_element(By.XPATH, "//*[@data-test='remove-sauce-labs-backpack']").text

    assert remove_button_text == 'Remove', 'Текст не соответствует'

#-Удаление товара из корзины через карточку товара
def test_delete_product_from_catalog():
    driver.get(URL_TEST)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(USERNAME)

    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    add_product_to_catalog = driver.find_element(By.XPATH, "//*[@data-test='add-to-cart-sauce-labs-backpack']").click()

    button_remove = driver.find_element(By.XPATH, "//*[@data-test='remove-sauce-labs-backpack']").click()

    add_product_to_catalog_after_delete = driver.find_element(By.XPATH, "//*[@data-test='add-to-cart-sauce-labs-backpack']")

    assert add_product_to_catalog_after_delete.text == 'Add to cart'

#-Удаление товара из корзины через корзину
def test_delete_product_from_cart():
    driver.get(URL_TEST)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(USERNAME)

    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    add_product_to_cart = driver.find_element(By.XPATH, "//*[@data-test='add-to-cart-sauce-labs-backpack']").click()

    driver.find_element(By.XPATH,CART_BUTTON).click()

    button_remove = driver.find_element(By.XPATH, "//*[@class='btn btn_secondary btn_small cart_button']").click()

    assert driver.current_url == 'https://www.saucedemo.com/cart.html'

# 3.Карточка ЦВЕТ
# -Успешный переход к карточке товара после клика на картинку товара
def test_clik_image():
    driver.get(URL_TEST)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(USERNAME)

    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()


    image_on_list = driver.find_element(By.XPATH, "//*[@id='item_0_img_link']/img").click()
    time.sleep(3)

    image_in_product_card = driver.find_element(By.XPATH,"//*[contains(text(),'Sauce Labs Bike Light')]")

    assert image_in_product_card.text == 'Sauce Labs Bike Light'

# -Успешный переход к карточке товара после клика по названию товара
def test_click_name_product():
    driver.get(url_test)

    username = driver.find_element(By.XPATH, "//*[@placeholder='Username']")
    username.send_keys('standard_user')

    password = driver.find_element(By.XPATH, "//*[@placeholder='Password']")
    password.send_keys('secret_sauce')

    button_login = driver.find_element(By.XPATH, "//*[@data-test='login-button']")
    button_login.click()

    protuct_text = driver.find_element(By.XPATH,"//div[normalize-space()='Sauce Labs Bolt T-Shirt']")
    protuct_text.click()

    assert driver.current_url =='https://www.saucedemo.com/inventory-item.html?id=1'

    time.sleep(2)


#  4.Оформление заказа
# -Оформление заказа с использованием корректных данных
def test_placing_an_order():
    driver.get(url_test)

    username = driver.find_element(By.XPATH, "//*[@placeholder='Username']")
    username.send_keys('standard_user')

    password = driver.find_element(By.XPATH, "//*[@placeholder='Password']")
    password.send_keys('secret_sauce')

    button_login = driver.find_element(By.XPATH, "//*[@data-test='login-button']")
    button_login.click()

    protuct_text = driver.find_element(By.XPATH, "//div[normalize-space()='Sauce Labs Bolt T-Shirt']")
    protuct_text.click()

    button_add = driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
    button_add.click()

    button_basket = driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']")
    button_basket.click()

    button_checkout = driver.find_element(By.XPATH,"//button[@id='checkout']")
    button_checkout.click()

    button_first_name = driver.find_element(By.XPATH,"//input[@id='first-name']")
    button_first_name.send_keys('Andrey')

    button_last_name = driver.find_element(By.XPATH,"//input[@id='last-name']")
    button_last_name.send_keys('Ivanov')

    button_zip = driver.find_element(By.XPATH, "//input[@id='postal-code']")
    button_zip.send_keys('3125')

    continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
    continue_button.click()

    finish_button = driver.find_element(By.XPATH, "//button[@id='finish']")
    finish_button.click()

    complete = driver.find_element(By.XPATH, "//h2[@class='complete-header']")

    assert complete.text == 'Thank you for your order!'


# Фильтр
# -Проверка работоспособности фильтра (от А до Я)
def test_asc():
    driver.get(url_test)
    username = driver.find_element(By.XPATH, "//*[@placeholder='Username']")
    username.send_keys('standard_user')

    password = driver.find_element(By.XPATH, "//*[@placeholder='Password']")
    password.send_keys('secret_sauce')

    button_login = driver.find_element(By.XPATH, "//*[@data-test='login-button']")
    button_login.click()

    button_serting = driver.find_element(By.XPATH, "//*[@value='az']")
    button_serting.click()

    time.sleep(2)


# -Проверка работоспособности фильтра (от Z до A)
def test_desc():
    driver.get(url_test)
    username = driver.find_element(By.XPATH, "//*[@placeholder='Username']")
    username.send_keys('standard_user')

    password = driver.find_element(By.XPATH, "//*[@placeholder='Password']")
    password.send_keys('secret_sauce')

    button_login = driver.find_element(By.XPATH, "//*[@data-test='login-button']")
    button_login.click()

    button_serting = driver.find_element(By.XPATH, "//*[@value='za']")
    button_serting.click()

    time.sleep(2)

# -Проверка работоспособности фильтра (от низкой до высокой)
def test_price_low():
    driver.get(url_test)

    username = driver.find_element(By.XPATH, "//*[@placeholder='Username']")
    username.send_keys('standard_user')

    password = driver.find_element(By.XPATH, "//*[@placeholder='Password']")
    password.send_keys('secret_sauce')

    button_login = driver.find_element(By.XPATH, "//*[@data-test='login-button']")
    button_login.click()

    button_serting = driver.find_element(By.XPATH, "//*[@value='lohi']")
    button_serting.click()

    time.sleep(2)

# -Проверка работоспособности фильтра (от высокой до низкой)
def test_price_higt():
    driver.get(url_test)

    username = driver.find_element(By.XPATH, "//*[@placeholder='Username']")
    username.send_keys('standard_user')

    password = driver.find_element(By.XPATH, "//*[@placeholder='Password']")
    password.send_keys('secret_sauce')

    button_login = driver.find_element(By.XPATH, "//*[@data-test='login-button']")
    button_login.click()

    button_serting = driver.find_element(By.XPATH, "//*[@value='hilo']")
    button_serting.click()
    time.sleep(2)

#  5.меню бургер
# -Выход из системы
def test_exit():
    driver.get(url_test)
    username = driver.find_element(By.XPATH, "//*[@placeholder='Username']")
    username.send_keys('standard_user')

    password = driver.find_element(By.XPATH, "//*[@placeholder='Password']")
    password.send_keys('secret_sauce')

    button_login = driver.find_element(By.XPATH, "//*[@data-test='login-button']")
    button_login.click()

    button_burger = driver.find_element(By.XPATH,"//*[@id='react-burger-menu-btn']")
    button_burger.click()
    time.sleep(1)

    button_logout = driver.find_element(By.XPATH,"//a[@id='logout_sidebar_link']")
    button_logout.click()
    time.sleep(1)

    assert driver.current_url == 'https://www.saucedemo.com/'


# -Проверка работоспособности кнопки «О программе» в меню
def test_about():
    driver.get(url_test)

    username = driver.find_element(By.XPATH, "//*[@placeholder='Username']")
    username.send_keys('standard_user')

    password = driver.find_element(By.XPATH, "//*[@placeholder='Password']")
    password.send_keys('secret_sauce')

    button_login = driver.find_element(By.XPATH, "//*[@data-test='login-button']")
    button_login.click()

    button_burger = driver.find_element(By.XPATH,"//*[@id='react-burger-menu-btn']")
    button_burger.click()
    time.sleep(1)

    button_about = driver.find_element(By.XPATH,"//a[@id='about_sidebar_link']")
    button_about.click()
    time.sleep(1)

    assert driver.current_url == 'https://saucelabs.com/'


# -Проверка работоспособности кнопки «Сбросить состояние приложения»
def test_reset():
    driver.get(url_test)

    username = driver.find_element(By.XPATH, "//*[@placeholder='Username']")
    username.send_keys('standard_user')

    password = driver.find_element(By.XPATH, "//*[@placeholder='Password']")
    password.send_keys('secret_sauce')

    button_login = driver.find_element(By.XPATH, "//*[@data-test='login-button']")
    button_login.click()

    button_burger = driver.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']")
    button_burger.click()
    time.sleep(1)

    button_reset = driver.find_element(By.XPATH, "//a[@id='reset_sidebar_link']")
    button_reset.click()

    driver.quit()



