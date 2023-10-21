from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from locators import USERNAME_FIELD, PASSWORD_FIELD,LOGIN_BUTTON,CART_BUTTON,BORGER_BUTTON
from data import URL_TEST, USERNAME, PASSWORD, PASSWORD_NOT_CORRECT, FIRST_NAME, LAST_NAME, ZIP_CODE,URL_PAGE
from selenium.webdriver.support import expected_conditions as EC


# 1.Авторизация
# авторизация с использованием корректных данных (standard_user, secret_sauce)
def test_avtorization_correct(driver,authorization):
    # driver.get(URL_TEST)
    # driver.maximize_window()
    # driver.find_element(By.XPATH,USERNAME_FIELD).send_keys(USERNAME)
    # driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)
    # driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'

# авторизация с использованием некорректных данных (пользователя)
def test_avtorization_not_correct(driver):
    driver.get(URL_TEST)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(USERNAME)

    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD_NOT_CORRECT)

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    error_field = driver.find_element(By.XPATH, "//*[@data-test='error']").text

    assert error_field == 'Epic sadface: Username and password do not match any user in this service'
    print(error_field)

# вывод текста плейсходера поля username
def test_text_plaseholder_username(driver):
    driver.get(URL_TEST)

    username_filed = driver.find_element(By.XPATH, USERNAME_FIELD)
    placeholder = username_filed.get_attribute('placeholder')

    assert placeholder == 'Username'
    print(placeholder)

# 2.Корзина
# проверка текста кнопки Remove
def test_add_product_to_catalog(driver,authorization):
    add_product_to_catalog = driver.find_element(By.XPATH, "//*[@data-test='add-to-cart-sauce-labs-backpack']").click()

    remove_button_text = driver.find_element(By.XPATH, "//*[@data-test='remove-sauce-labs-backpack']").text

    assert remove_button_text == 'Remove', 'Текст не соответствует'

# проверка количества товара в иконке корзины
def test_quantity_incart(driver,authorization):
    add_product_to_cart = driver.find_element(By.XPATH, "//*[@data-test='add-to-cart-sauce-labs-backpack']").click()

    cart = driver.find_element(By.XPATH,CART_BUTTON).text

    assert cart == '1'

# Добавдение и удаления товара с помощью кнопки Add to cart
def test_delete_product_from_catalog(driver,authorization):
    add_product_to_catalog = driver.find_element(By.XPATH, "//*[@data-test='add-to-cart-sauce-labs-backpack']").click()

    button_remove = driver.find_element(By.XPATH, "//*[@data-test='remove-sauce-labs-backpack']").click()

    add_product_to_catalog_after_delete = driver.find_element(By.XPATH, "//*[@data-test='add-to-cart-sauce-labs-backpack']").text

    assert add_product_to_catalog_after_delete == 'Add to cart'
    print(add_product_to_catalog_after_delete)

#-Удаление товара из корзины через кнопку remove
def test_delete_product_from_cart(driver,authorization):
    add_product_to_cart = driver.find_element(By.XPATH, "//*[@data-test='add-to-cart-sauce-labs-backpack']").click()

    driver.find_element(By.XPATH, CART_BUTTON).click()

    button_remove = driver.find_element(By.XPATH, "//*[@class='btn btn_secondary btn_small cart_button']").click()

    assert driver.current_url == 'https://www.saucedemo.com/cart.html'

#-Удаление товара из корзины, проверка что корзина пуста
def test_delete_product_from_cart_new(driver, authorization):
    add_product_to_cart = driver.find_element(By.XPATH, "//*[@data-test='add-to-cart-sauce-labs-backpack']").click()

    driver.find_element(By.XPATH, CART_BUTTON).click()

    button_remove = driver.find_element(By.XPATH, "//*[@class='btn btn_secondary btn_small cart_button']").click()
    time.sleep(1)

    try:
        driver.find_element(By.XPATH, "//*[@data-test='add-to-cart-sauce-labs-backpack']")
        assert False, 'There are items in the cart'
    except NoSuchElementException:
        assert True

# 3.Карточка ЦВЕТ
# переход к карточке товара после клика на картинку товара
def test_clik_image(driver, authorization):
    image_on_list_after = driver.find_element(By.XPATH, "//*[contains(text(),'Sauce Labs Bike Light')]").text
    print("Текст в каталоге - " + image_on_list_after)
    image_on_list = driver.find_element(By.XPATH, "//*[contains(text(),'Sauce Labs Bike Light')]").click()

    image_in_list_before = driver.find_element(By.XPATH,"//*[contains(text(),'Sauce Labs Bike Light')]").text
    print("Текст в карточке товара - " + image_in_list_before)

    assert image_on_list_after == image_in_list_before

# -Успешный переход к карточке товара после клика по названию товара
def test_click_name_product(driver, authorization):
    driver.find_element(By.XPATH,"//div[normalize-space()='Sauce Labs Bolt T-Shirt']").click()
    time.sleep(1)

    cart_product = driver.find_element(By.XPATH,"//div[@class='inventory_details_name large_size']")

    assert cart_product.text =='Sauce Labs Bolt T-Shirt'

#  4.Оформление заказа
# end-to-end формление заказа с использованием корректных данных
def test_placing_an_order(driver,authorization):
    driver.find_element(By.XPATH, "//div[normalize-space()='Sauce Labs Bolt T-Shirt']").click()

    driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()

    driver.find_element(By.XPATH, CART_BUTTON).click()
    time.sleep(3)

    driver.find_element(By.XPATH,"//button[@id='checkout']").click()

    driver.find_element(By.XPATH,"//input[@id='first-name']").send_keys(FIRST_NAME)
    driver.find_element(By.XPATH,"//input[@id='last-name']").send_keys(LAST_NAME)
    driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys(ZIP_CODE)

    authorization.find_element(By.XPATH, "//input[@id='continue']").click()
    driver.find_element(By.XPATH, "//button[@id='finish']").click()
    complete = authorization.find_element(By.XPATH, "//h2[@class='complete-header']").text

    assert complete == 'Thank you for your order!'

# Фильтр
# проверка работоспособности фильтра (от А до Я)
def test_filter_name_asc(driver,authorization):
    driver.find_element(By.XPATH, "//*[@value='az']").click()

    button_serting = driver.find_element(By.XPATH, "//*[@value='az']")

    assert button_serting.text == 'Name (A to Z)'

# проверка работоспособности фильтра (от Z до A)
def test_filter_name_desc(driver,authorization):
    driver.find_element(By.XPATH, "//*[@value='za']").click()

    button_serting = driver.find_element(By.XPATH, "//*[@value='za']").text

    assert button_serting == 'Name (Z to A)'

# проверка работоспособности фильтра (от низкой до высокой)
def test_filter_price_low(driver,authorization):
    driver.find_element(By.XPATH, "//*[@value='lohi']").click()

    button_serting = driver.find_element(By.XPATH, "//*[@value='lohi']")

    assert button_serting.text == 'Price (low to high)'

# проверка работоспособности фильтра (от высокой до низкой)
def test_filter_price_higt(driver,authorization):
    driver.find_element(By.XPATH, "//*[@value='hilo']").click()

    button_serting = driver.find_element(By.XPATH, "//*[@value='hilo']")

    assert button_serting.text == 'Price (high to low)'

#  5.меню бургер
# выход из системы
def test_exit_through_burger(driver,authorization):
    driver.find_element(By.XPATH,BORGER_BUTTON).click()
    time.sleep(1)

    button_logout = driver.find_element(By.XPATH,"//a[@id='logout_sidebar_link']").click()
    time.sleep(1)

    assert driver.current_url == URL_PAGE

# проверка работоспособности кнопки «О программе» в меню
def test_about(driver,authorization):
    driver.find_element(By.XPATH, BORGER_BUTTON).click()
    time.sleep(1)

    button_about = driver.find_element(By.XPATH,"//a[@id='about_sidebar_link']").click()
    time.sleep(1)

    assert driver.current_url == 'https://saucelabs.com/'

# -Проверка работоспособности кнопки «Сбросить состояние приложения»
def test_reset(driver,authorization):
    driver.find_element(By.XPATH, BORGER_BUTTON).click()
    time.sleep(1)

    button_reset = driver.find_element(By.XPATH, "//a[@id='reset_sidebar_link']").is_enabled()

    assert button_reset == True

# отображение,взаимодействие,вывод тега элемента в катологе у кнопки 'Add to cart'

def test_button_add(driver,authorization):
    button_add = driver.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-backpack']")

    assert button_add.is_displayed()
    assert button_add.is_enabled()
    assert button_add.tag_name
    print("Тег у элемента ->" + button_add.tag_name)

# Задание 2
#проверка что чекбокс не выбран Ссылка: https://victoretc.github.io/webelements_information/
def test_checkbox_off(driver):
    driver.get('https://victoretc.github.io/webelements_information/')

    driver.find_element(By.XPATH,"//*[@id='username']").send_keys(FIRST_NAME)

    driver.find_element(By.XPATH, "//*[@id='password']").send_keys(ZIP_CODE)

    checkbox_not_click = driver.find_element(By.XPATH, "//*[@id='agreement']")

    assert checkbox_not_click.is_selected() == False
    driver.quit()

# проверка что чекбокс выбран, видимый, доступный для взаимодействия
def test_checkbox_on(driver):
    driver.get('https://victoretc.github.io/webelements_information/')

    driver.find_element(By.XPATH, "//*[@id='username']").send_keys(FIRST_NAME)
    driver.find_element(By.XPATH, "//*[@id='password']").send_keys(ZIP_CODE)

    checkbox = driver.find_element(By.XPATH, "//*[@id='agreement']")
    if not checkbox.is_selected():
        checkbox.click()

    assert checkbox.is_displayed()
    assert checkbox.is_enabled() == True
    assert checkbox.is_selected() == True




