from locators import TEST_TAG,BUTTON_START_TEST,LOGIN_FIELD,CHECXBOX,REGISTER_BUTTON,LOADER,FINAL_MASSAGE,PASSWORD_FIELD
from data import URL_TEST,LOGIN,PASSWORD
from selenium.webdriver.support import expected_conditions as EC
from pytest_course.hw4.waits_hw.registration.conftest import *



def test_registration(driver,wait):
    driver.get(URL_TEST)
    assert driver.current_url == 'https://victoretc.github.io/selenium_waits/'

    test_tag = wait.until(EC.visibility_of_element_located(TEST_TAG))
    assert test_tag.text == "Практика с ожиданиями в Selenium"

    button_start_test = wait.until(EC.element_to_be_clickable(BUTTON_START_TEST))
    # button_start_test = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_START_TEST))
    assert 'Начать тестирование' in button_start_test.text
    button_start_test.click()

    login_field = wait.until(EC.visibility_of_element_located(LOGIN_FIELD))
    login_field.clear()
    login_field.send_keys(LOGIN)

    password_field = wait.until(EC.visibility_of_element_located(PASSWORD_FIELD))
    password_field.clear()
    password_field.send_keys(PASSWORD)

    checxbox = wait.until(EC.visibility_of_element_located(CHECXBOX))
    checxbox.click()
    assert checxbox.is_selected() == True

    button_register = wait.until(EC.visibility_of_element_located(REGISTER_BUTTON))
    button_register.text == 'Зарегистрироваться'
    button_register.click()

    loader = wait.until(EC.visibility_of_all_elements_located(LOADER))
    # assert loader.is_displayed()==True
    # assert loader.text =='Загрузка...'

    final_massage = wait.until(EC.element_to_be_clickable(FINAL_MASSAGE))
    assert final_massage.text == "Вы успешно зарегистрированы!",'Регистрация не прошла'
    print(final_massage.text)



