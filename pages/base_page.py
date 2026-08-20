from locators import base_page_locators
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
import allure
from seletools.actions import drag_and_drop


class BasePage():
    base_url = "https://qa-stellarburgers.education-services.ru/"
    base_timeout = 10

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_for_main_screen(self):
        self.wait_for_element(base_page_locators.constructor_header)
    
    @allure.step('Клик по логотипу "Stellar Burgers"')
    def click_on_stellar_burgers_logo(self):
        self.click_on_element(base_page_locators.stellar_burger_icon)

    @allure.step('Ожидание элемента')
    def wait_for_element(self, locator):
        WebDriverWait(self.driver, self.base_timeout).until(EC.visibility_of_element_located(locator))
    
    @allure.step('Клик на элемент')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Ввод текста в инпутное поле')
    def input_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)
    
    def check_visibility(self, locator):
        return self.driver.find_element(*locator).is_displayed()
    
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def get_text_of_the_element(self, locator):
        return self.find_element(locator).text

    @allure.step('Перетаскивание элемента')
    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        drag_and_drop(self.driver, source, target)

    def get_element_attribute(self, locator, attribute:str):
        element = self.find_element(locator)
        return element.get_attribute(attribute)

    def hide_modal(self):
        self.driver.execute_script("""document.querySelectorAll('.Modal_modal_overlay__x2ZCr, [class*="Modal"]').forEach(el => el.style.display = 'none');""")

    def show_modal(self):
        self.driver.execute_script("""document.querySelectorAll('.Modal_modal_overlay__x2ZCr, [class*="Modal"]').forEach(el => el.style.display = '');""")

    def wait_for_text_to_change(self, locator, old_text):
        WebDriverWait(self.driver, self.base_timeout).until(lambda d: d.find_element(*locator).text != old_text)
        return self.driver.find_element(*locator).text

    @allure.step('Фокус мыши на элемент')
    def move_to_element(self, locator):
        element = self.find_element(locator)
        AC(self.driver).move_to_element(element).click().perform()

    @allure.step('Клик на элемент')
    def js_click(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def wait_for_text_to_appear(self, locator, expected_text):
        WebDriverWait(self.driver, self.base_timeout).until(lambda d: d.find_element(*locator).text == expected_text)
        return self.driver.find_element(*locator).text