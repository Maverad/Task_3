from pages.profile_page import ProfilePage
from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage
import pytest
from selenium import webdriver
from helpers import GenerateTestData as GD
import requests
import os


base_url = 'https://qa-stellarburgers.education-services.ru/'
url_auth = 'https://qa-stellarburgers.education-services.ru/api/auth/register'
url_delete_profile = 'https://qa-stellarburgers.education-services.ru/api/auth/user'

@pytest.fixture
def driver():
    browser = os.getenv('BROWSER', 'chrome').lower()
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(base_url)
    yield driver
    driver.quit()

@pytest.fixture
def login_profile(new_user_api, profile):
    _, user, _ = new_user_api
    profile.user_login(user.get('email'), user.get('password'))
    profile.wait_for_main_screen()
    return profile

@pytest.fixture
def new_user_api():
    generate = GD()
    user = {
        'email': generate.generate_random_email(7).lower(),
        'password': generate.generate_random_password(10),
        'name': generate.generate_random_name(6).lower()
        }
    response = requests.post(url_auth, user)
    data = response.json()
    token = data.get('accessToken')
    headers = {
            "Authorization": token
        }
    yield (response, user, token)
    requests.delete(url_delete_profile, headers=headers)

@pytest.fixture
def constructor(driver):
    constructor = ConstructorPage(driver)
    return constructor

@pytest.fixture
def profile(driver):
    profile = ProfilePage(driver)
    return profile

@pytest.fixture
def order(driver):
    order = OrderFeedPage(driver)
    return order

