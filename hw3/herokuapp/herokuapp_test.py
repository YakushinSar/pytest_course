from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from locators import BUTTON_ADD_ELEMENT, BUTTON_DELETE
import time



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


