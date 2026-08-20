import allure


class TestConstructor:

    @allure.title('Проверка позитивного флоу создания заказа')
    def test_create_order(self, constructor, order, login_profile):
        constructor.hide_modal()
        constructor.create_order()
        constructor.show_modal()
        constructor.wait_for_order_modal()
        order_id = '0' + constructor.get_order_id_counter()

        assert constructor.check_create_order_success()

        constructor.hide_modal()
        order.click_on_order_feed()
        order.wait_for_order_feed_screen()
        constructor.show_modal()
        order_id_on_feed_screen = order.last_order_by_id().replace('#', '')
        
        assert order_id == order_id_on_feed_screen

    @allure.title('Проверка модального окна ингридиента')
    def test_ingredient_modal(self, constructor):
        constructor.hide_modal()
        constructor.click_on_ingredient()

        assert constructor.check_ingredient_modal()
        
        constructor.close_modal()

    @allure.title('Проверка изменения каунтера ингридиента')
    def test_ingredient_counter(self, constructor):
        constructor.hide_modal()
        bun_count_before = constructor.get_bun_counter()
        sauce_count_before = constructor.get_sauce_counter()
        constructor.add_bun()
        constructor.add_sauce()
        bun_count_after = constructor.get_bun_counter()
        sauce_count_after = constructor.get_sauce_counter()

        assert bun_count_before == 0 and bun_count_after == 2
        assert sauce_count_before == 0 and sauce_count_after == 1

