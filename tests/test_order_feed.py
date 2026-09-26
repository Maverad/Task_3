import allure


class TestOrderFeed:

    @allure.title('Проверка открытия модального окна заказа')
    def test_order_details_open(self, order):
        order.hide_modal()
        order.click_on_order_feed()
        order.wait_for_order_feed_screen()
        order.click_on_last_order()
        order.show_modal()
        order.wait_for_order_modal()

        assert order.check_order_modal_visible()

    @allure.title('Проверка закрытия модального окна заказа')
    def test_order_details_close(self, order):
        order.hide_modal()
        order.click_on_order_feed()
        order.wait_for_order_feed_screen()
        order.click_on_last_order()
        order.show_modal()
        order.remove_modal_overlay()
        order.wait_for_order_modal()
        order.close_order_modal()

        assert order.check_order_modal_invisible()

    @allure.title('Проверка увеличения счетчика "Выполнено за все время"')
    def test_counter_all_time(self, order, constructor, login_profile):
        order.hide_modal()
        order.click_on_order_feed()
        order.wait_for_order_feed_screen()
        counter_before = order.get_all_time_counter()
        constructor.click_on_constructor()
        constructor.create_order()
        order.click_on_order_feed()
        order.wait_for_order_feed_screen()
        counter_after = order.get_all_time_counter()

        assert counter_before < counter_after

    @allure.title('Проверка увеличения счетчика "Выполнено за сегодня"')
    def test_counter_today(self, order, constructor, login_profile):
        order.hide_modal()
        order.click_on_order_feed()
        order.wait_for_order_feed_screen()
        counter_before = order.get_today_counter()
        constructor.click_on_constructor()
        constructor.create_order()
        order.click_on_order_feed()
        order.wait_for_order_feed_screen()
        counter_after = order.get_today_counter()
        
        assert counter_before < counter_after

    @allure.title('Проверка созданного заказа в блоке "В работе"')
    def test_order_in_progress(self, order, constructor, login_profile):
        order.hide_modal()
        constructor.create_order()
        constructor.show_modal()
        constructor.wait_for_order_modal()
        order_id = '0' + constructor.get_order_id_counter()
        constructor.remove_modal_overlay()
        constructor.close_modal()
        constructor.hide_modal()
        order.click_on_order_feed()
        order.wait_for_order_feed_screen()
        order.order_in_progress_check(order_id)
        
        assert order_id == order.get_in_progress_id()