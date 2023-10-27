import requests
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from locators import *
import time

# 1. https://the-internet.herokuapp.com/add_remove_elements/ (Необходимо создать и удалить элемент)
def test_add_remove_elements(driver, wait):
    driver.get( 'https://the-internet.herokuapp.com/add_remove_elements/')
    add_element =driver.find_element(By.XPATH, BUTTON_ADD_ELEMENT)
    assert add_element.text == 'Add Element'
    assert add_element.is_enabled()
    add_element.click()

    delete_buttons = driver.find_element(By.XPATH, BUTTON_DELETE)
    delete_buttons.is_displayed()==True
    delete_buttons.click()

    number_of_delete_buttons_after = driver.find_elements(By.XPATH, BUTTON_DELETE)
    assert len(number_of_delete_buttons_after) == 0, 'Кнопка отображается'

# 2. https://the-internet.herokuapp.com/basic_auth (Необходимо пройти базовую авторизацию)
def test_basic_auth(driver,wait):
    driver.get('//the-internet.herokuapp.com/basic_auth')
    text_success_auth = driver.find_element(By.XPATH, '//p[contains(text(), "Congratulations!")]').text
    assert driver.find_element(By.XPATH, '//h3').text == 'Basic Auth'
    assert text_success_auth == 'Congratulations! You must have the proper credentials.'

# 3. https://the-internet.herokuapp.com/broken_images (Необходимо найти сломанные изображения)
def test_broken_images(driver):
    driver.get('//the-internet.herokuapp.com/broken_images')
    list_images = driver.find_elements(By.XPATH, IMG_ANY)
    list_img_links = []

    for image in range(1, len(list_images) + 1):
        image_link = driver.find_element(By.XPATH,
                                            f'{IMG_ANY}[{image}]').get_property("src")
        list_img_links.append(image_link)

    list_broken_links = []
    list_correct_links = []
    for link in list_img_links:
        response = requests.get(link)
        if response.status_code != 200:
            list_broken_links.append(link)
        else:
            list_correct_links.append(link)

    assert len(list_broken_links) == 0, f"\n{len(list_broken_links)} broken link(s): {list_broken_links} \n{len(list_correct_links)} correct link(s): {list_correct_links}"

# 4. https://the-internet.herokuapp.com/checkboxes (Практика с чек боксами)



