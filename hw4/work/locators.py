from selenium.webdriver.common.by import By

LOGIN_FIELD = (By.XPATH,"// *[ @ id = 'login']")
PASSWORD_FIELD = (By.XPATH,"// *[ @ id = 'password']")
CHECXBOX = (By.XPATH,"//*[@type='checkbox']")
REGISTER_BUTTON = (By.XPATH,"//*[@id='register']")
BUTTON_START_TEST = (By.XPATH,'//button[@id="startTest"]')
FINAL_MASSAGE = (By.XPATH,'//p[@id="successMessage"][@class=""]')

# #распаковка идет по такому способу
# def sum_of_values(a, b, c):
#     return a + b + c
#
# values = [1, 2, 3]
# result = sum_of_values(*values)
# print(result)