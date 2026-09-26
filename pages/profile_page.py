from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators as locator
import allure


class ProfilePage(BasePage):

    def wait_for_login_profile_screen(self):
        self.wait_for_element(locator.exit_from_profile)

    def wait_for_login_screen(self):
        self.wait_for_element(locator.login_button)

    def wait_for_new_password_screen(self):
        self.wait_for_element(locator.new_password_input)

    def wait_for_reset_password_screen(self):
        self.wait_for_element(locator.email_input_reset_password_screen)

    @allure.step('Клик по логотипу "Личный кабинет"')
    def click_on_profile(self):
        self.click_on_element(locator.profile)

    @allure.step('Клик на кнопку восстановления пароля')
    def click_on_reset_password(self):
        self.click_on_element(locator.reset_password)

    @allure.step('Ввод email в инпутное поле на экране восстановления пароля')
    def input_email_for_reset_password(self):
        self.input_text(locator.email_input_reset_password_screen, 'test@ya.ru')

    @allure.step('Клик на кнопку "Восстановить" на экране восстановления пароля')
    def click_on_reset_password_submit(self):
        self.click_on_element(locator.reset_password_submit)

    @allure.step('Ввод нового пароля')
    def input_new_password(self):
        self.input_text(locator.new_password_input, 'test')

    @allure.step('Ввод email в инпутное поле на экране логина')
    def input_email_login_screen(self, email):
        self.input_text(locator.email_input_login_screen, email)

    @allure.step('Ввод пароля в инпутное поле на экране логина')
    def input_password_login_screen(self, password):
        self.input_text(locator.password_input_login_screen, password)

    @allure.step('Клик на кнопку логина')
    def click_on_login_button(self):
        self.click_on_element(locator.login_button)

    @allure.step('Клик на историю заказов в профиле')
    def click_on_order_history(self):
        self.click_on_element(locator.order_history)

    @allure.step('Клик на "Выход" в профиле')
    def click_on_exit(self):
        self.click_on_element(locator.exit_from_profile)

    @allure.step('Логин пользователя')
    def user_login(self, email, password):
        self.click_on_profile()
        self.wait_for_login_screen()
        self.input_email_login_screen(email)
        self.input_password_login_screen(password)
        self.click_on_element(locator.login_button)

    def get_new_password_input_attribute(self, attribute:str):
        return self.get_element_attribute(locator.new_password_input, attribute)

    @allure.step('Клик на иконку глаза')
    def click_on_eye_button_new_password_screen(self):
        self.click_on_element(locator.new_password_eye_icon)

    def check_visibility_login_button(self):
        return self.check_visibility(locator.login_button)

    def check_visibility_order_history(self):
        return self.check_visibility(locator.order_history_item)
