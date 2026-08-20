from selenium.webdriver.common.by import By


class ProfilePageLocators:
    # Reset password screen:
    reset_password = (By.XPATH, './/a[text()="Восстановить пароль"]')
    email_input_reset_password_screen = (By.XPATH, './/input[@class="text input__textfield text_type_main-default"]')
    reset_password_submit = (By.XPATH, './/button[text()="Восстановить"]')
    new_password_input = (By.XPATH, './/input[@name="Введите новый пароль"]')
    new_password_eye_icon = (By.XPATH, './/div[@class="input__icon input__icon-action"]')

    # Login screen:
    email_input_login_screen = (By.XPATH, './/input[@class="text input__textfield text_type_main-default" and @name="name"]')
    password_input_login_screen = (By.XPATH, './/input[@class="text input__textfield text_type_main-default" and @name="Пароль"]')
    login_button = (By.XPATH, './/button[text()="Войти"]')
    modal_section_1 = (By.XPATH, './/section[@class="Modal_modal__P3_V5"]')
    modal_section_2 = (By.XPATH, './/div[@class="Modal_modal__P3_V5"]')

    # Profile screen
    order_history = (By.XPATH, './/a[text()="История заказов"]')
    order_history_item = (By.XPATH, './/div[@class="Account_contentBox__2CPm3"]')
    exit_from_profile = (By.XPATH, './/button[text()="Выход"]')
    login_profile = (By.XPATH, './/a[text()="Профиль"]')

    modal_for_delete = (By.XPATH, './/div[@class="Modal_modal_overlay__x2ZCr"]')
    profile = (By.XPATH, './/p[text()="Личный Кабинет"]')
