from selenium.webdriver.common.by import By


class ConstructorPageLocators:
    constructor = (By.XPATH, './/p[text()="Конструктор"]')
    constructor_header = (By.XPATH, './/h1[text()="Соберите бургер"]')
    create_order_button = (By.XPATH, './/button[text()="Оформить заказ"]')
    order_in_progress_modal = (By.XPATH, './/p[text()="Ваш заказ начали готовить"]')
    order_id = (By.XPATH, './/h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]')
    close_modal = (By.XPATH, '(.//button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"])[1]')
    bun = (By.XPATH, '(.//a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"])[1]')
    sauce = (By.XPATH, './/a[@href="/ingredient/691577430cc94f001a65b862"]')
    target_for_ingedients = (By.XPATH, './/div[@class="constructor-element constructor-element_pos_top"]')
    ingredients_in_order_counter_bun = (By.XPATH, '(.//p[@class="counter_counter__num__3nue1"])[1]')
    ingredients_in_order_counter_sauce = (By.XPATH, '(.//p[@class="counter_counter__num__3nue1"])[3]')
    ingredient_modal_check = (By.XPATH, './/h2[text()="Детали ингредиента"]')
    order_modal_animation = (By.XPATH, './/img[@class="Modal_modal__image__2nh17" and @alt="tick animation"]')
