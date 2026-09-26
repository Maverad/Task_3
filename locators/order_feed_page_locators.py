from selenium.webdriver.common.by import By


class OrderFeedPage:
    order_all_time = (By.XPATH, '(.//p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"])[1]')
    order_today_done = (By.XPATH, '(.//p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"])[2]')
    order_in_progress = (By.XPATH, './/ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li[@class="text text_type_digits-default mb-2"]')
    order_done_list = (By.XPATH, './/ul[@class="OrderFeed_orderList__cBvyi"]/li[@class="text text_type_digits-default mb-2"]')
    last_order = (By.XPATH, '(.//li[@class="OrderHistory_listItem__2x95r mb-6"])[1]')
    last_order_id = (By.XPATH, '(.//p[@class="text text_type_digits-default"])[1]')
    order_modal_opened = (By.XPATH, './/section[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]')
    order_modal_closed = (By.XPATH, '(.//section[@class="Modal_modal__P3_V5"])[1]')
    close_order_modal = (By.XPATH, '(.//button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"])[2]')
    order_modal_check = (By.XPATH, './/p[text()="Cостав"]')
    order_feed = (By.XPATH, './/p[text()="Лента Заказов"]')
