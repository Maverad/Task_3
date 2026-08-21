import allure


class TestProfile:

    @allure.title('Проверка функционала сброса пароля')
    def test_reset_password(self, profile):
        profile.hide_modal()
        profile.click_on_profile()
        profile.wait_for_login_screen()
        profile.click_on_reset_password()
        profile.wait_for_reset_password_screen()
        profile.input_email_for_reset_password()
        profile.click_on_reset_password_submit()
        profile.wait_for_new_password_screen()
        profile.input_new_password()
        profile.click_on_eye_button_new_password_screen()

        assert profile.get_new_password_input_attribute('type') == 'text'

    @allure.title('Проверка появления созданного заказа в профиле')
    def test_new_order_in_profile_history(self, profile, constructor, login_profile):
        profile.hide_modal()
        profile.wait_for_main_screen()
        constructor.create_order()
        profile.click_on_profile()
        profile.wait_for_login_profile_screen()
        profile.click_on_order_history()

        assert profile.check_visibility_order_history()

    @allure.title('Проверка разлогина пользователя')
    def test_exit_from_profile(self, profile, login_profile):
        profile.hide_modal()
        profile.click_on_profile()
        profile.wait_for_login_profile_screen()
        profile.click_on_exit()
        profile.wait_for_login_screen()

        assert profile.check_visibility_login_button()
