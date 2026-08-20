from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPage as locator
import allure


class OrderFeedPage(BasePage):

    def wait_for_order_feed_screen(self):
        self.wait_for_element(locator.last_order)

    def wait_for_order_modal(self):
        self.wait_for_element(locator.order_modal_opened)

    @allure.step('Клик по логотипу "Лента заказов"')
    def click_on_order_feed(self):
        self.click_on_element(locator.order_feed)

    @allure.step('Клик на последний заказ')
    def click_on_last_order(self):
        self.click_on_element(locator.last_order)

    @allure.step('Закрытие модального окна заказа')
    def close_order_modal(self):
        self.move_to_element(locator.close_order_modal)
        self.js_click(locator.close_order_modal)

    def last_order_by_id(self):
        last_order_id = self.get_text_of_the_element(locator.last_order_id)
        last_order_id.replace('#', '')
        return last_order_id

    def check_order_modal_visible(self):
        return self.check_visibility(locator.order_modal_check)

    def get_all_time_counter(self):
        return int(self.get_text_of_the_element(locator.order_all_time))

    def get_today_counter(self):
        return int(self.get_text_of_the_element(locator.order_today_done))
        
    def get_in_progress_id(self):
        self.wait_for_element(locator.order_in_progress)
        return self.get_text_of_the_element(locator.order_in_progress)

    def order_in_progress_check(self, text):
        self.wait_for_text_to_appear(locator.order_in_progress, text)
