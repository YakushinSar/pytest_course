from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from locators import USERNAME_FIELD, PASSWORD_FIELD,LOGIN_BUTTON,CART_BUTTON,BORGER_BUTTON
from data import URL_TEST, USERNAME, PASSWORD, PASSWORD_NOT_CORRECT, FIRST_NAME, LAST_NAME, ZIP_CODE,URL_PAGE
from selenium.webdriver.support import expected_conditions as EC

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

    remove_button_text = driver.find_element(By.XPATH, "//*[@data-test='remove-sauce-labs-backpack']")

    assert remove_button_text.text == 'Remove', 'Текст не соответствует'

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
    time.sleep(2)

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
    driver.get(URL_TEST)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(USERNAME)

    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    driver.find_element(By.XPATH,"//div[normalize-space()='Sauce Labs Bolt T-Shirt']").click()
    time.sleep(1)

    cart_product = driver.find_element(By.XPATH,"//div[@class='inventory_details_name large_size']")

    assert cart_product.text =='Sauce Labs Bolt T-Shirt'

#  4.Оформление заказа
# -Оформление заказа с использованием корректных данных
def test_placing_an_order():
    driver.get(URL_TEST)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(USERNAME)

    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    driver.find_element(By.XPATH, "//div[normalize-space()='Sauce Labs Bolt T-Shirt']").click()

    driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()

    driver.find_element(By.XPATH, CART_BUTTON).click()
    time.sleep(3)

    driver.find_element(By.XPATH,"//button[@id='checkout']").click()

    driver.find_element(By.XPATH,"//input[@id='first-name']").send_keys(FIRST_NAME)

    driver.find_element(By.XPATH,"//input[@id='last-name']").send_keys(LAST_NAME)

    driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys(ZIP_CODE)

    driver.find_element(By.XPATH, "//input[@id='continue']").click()

    driver.find_element(By.XPATH, "//button[@id='finish']").click()

    complete = driver.find_element(By.XPATH, "//h2[@class='complete-header']")

    assert complete.text == 'Thank you for your order!'

# Фильтр
# -Проверка работоспособности фильтра (от А до Я)
def test_filter_name_asc():
    driver.get(URL_TEST)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(USERNAME)

    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    driver.find_element(By.XPATH, "//*[@value='az']").click()

    button_serting = driver.find_element(By.XPATH, "//*[@value='az']")

    assert button_serting.text == 'Name (A to Z)'

# -Проверка работоспособности фильтра (от Z до A)
def test_filter_name_desc():
    driver.get(URL_TEST)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(USERNAME)

    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    driver.find_element(By.XPATH, "//*[@value='za']").click()

    button_serting = driver.find_element(By.XPATH, "//*[@value='za']")

    assert button_serting.text == 'Name (Z to A)'

# -Проверка работоспособности фильтра (от низкой до высокой)
def test_filter_price_low():
    driver.get(URL_TEST)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(USERNAME)

    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    driver.find_element(By.XPATH, "//*[@value='lohi']").click()

    button_serting = driver.find_element(By.XPATH, "//*[@value='lohi']")

    assert button_serting.text == 'Price (low to high)'

# -Проверка работоспособности фильтра (от высокой до низкой)
def test_filter_price_higt():
    driver.get(URL_TEST)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(USERNAME)

    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    driver.find_element(By.XPATH, "//*[@value='hilo']").click()

    button_serting = driver.find_element(By.XPATH, "//*[@value='hilo']")

    assert button_serting.text == 'Price (high to low)'

#  5.меню бургер
# -Выход из системы
def test_exit_through_burger():
    driver.get(URL_TEST)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(USERNAME)

    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    driver.find_element(By.XPATH,BORGER_BUTTON).click()
    time.sleep(1)

    button_logout = driver.find_element(By.XPATH,"//a[@id='logout_sidebar_link']").click()
    time.sleep(1)

    assert driver.current_url == URL_PAGE

# -Проверка работоспособности кнопки «О программе» в меню
def test_about():
    driver.get(URL_TEST)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(USERNAME)

    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    driver.find_element(By.XPATH, BORGER_BUTTON).click()
    time.sleep(1)

    button_about = driver.find_element(By.XPATH,"//a[@id='about_sidebar_link']").click()
    time.sleep(1)

    assert driver.current_url == 'https://saucelabs.com/'

# -Проверка работоспособности кнопки «Сбросить состояние приложения»
def test_reset():
    driver.get(URL_TEST)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(USERNAME)

    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    driver.find_element(By.XPATH, BORGER_BUTTON).click()
    time.sleep(1)

    button_reset = driver.find_element(By.XPATH, "//a[@id='reset_sidebar_link']").click()

def test_button_add():
    driver.get(URL_TEST)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(USERNAME)

    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    button_add = driver.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-backpack']")

    assert button_add.is_displayed()
    assert button_add.is_enabled()
    assert button_add.tag_name
    assert button_add.text == 'Add to cart'

    driver.quit()

def test_checkbox():
    driver.get('https://victoretc.github.io/webelements_information/')

    driver.find_element(By.XPATH,"//*[@id='username']").send_keys(FIRST_NAME)

    driver.find_element(By.XPATH, "//*[@id='password']").send_keys(ZIP_CODE)

    checkbox_not_click = driver.find_element(By.XPATH, "//*[@id='agreement']")
    time.sleep(2)

    checkbox = driver.find_element(By.XPATH, "//*[@id='agreement']")
    if not checkbox.is_selected():
        checkbox.click()
    time.sleep(3)

    assert checkbox_not_click.is_displayed()
    assert checkbox_not_click.is_enabled() == True
    assert checkbox.is_selected() == True

    driver.quit()



