from pages.base_page import BasePage
from locators.constructor_page_locators import ConstructorPageLocators as locator
import allure


class ConstructorPage(BasePage):

    def wait_for_constructor(self):
        self.wait_for_element(locator.bun)

    def wait_for_order_modal(self):
        self.wait_for_element(locator.order_modal_animation)

    @allure.step('Клик по логотипу "Конструктор"')
    def click_on_constructor(self):
        self.click_on_element(locator.constructor)

    @allure.step('Добавление булочки')
    def add_bun(self):
        self.drag_and_drop(locator.bun, locator.target_for_ingedients)

    @allure.step('Добавление соуса')
    def add_sauce(self):
        self.drag_and_drop(locator.sauce, locator.target_for_ingedients)

    @allure.step('Клик на ингридиент')
    def click_on_ingredient(self):
        self.click_on_element(locator.bun)

    @allure.step('Закрытие модального окна ингридиента')
    def close_modal(self):
        self.click_on_element(locator.close_modal)

    @allure.step('Клик на кнопку создания заказа')
    def click_on_create_order_button(self):
        self.click_on_element(locator.create_order_button)

    @allure.step('Позитивный флоу создания заказа')
    def create_order(self):
        self.add_bun()
        self.add_sauce()
        self.click_on_create_order_button()

    def get_bun_counter(self):
        return int(self.get_text_of_the_element(locator.ingredients_in_order_counter_bun))

    def get_sauce_counter(self):
        return int(self.get_text_of_the_element(locator.ingredients_in_order_counter_sauce))

    def check_ingredient_modal(self):
        return self.check_visibility(locator.ingredient_modal_check)

    def check_create_order_success(self):
        return self.check_visibility(locator.order_id)

    def get_order_id_counter(self):
        old_text = self.get_text_of_the_element(locator.order_id)
        return self.wait_for_text_to_change(locator.order_id, old_text)
