import pytest
import requests
from selenium import webdriver

from helpers import Helpers

from const import Ingredients, API
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.personal_page import PersonalPage
from pages.recovery_page import RecoveryPage


@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    elif request.param == "firefox":
        web_driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {request.param}")
    web_driver.browser_name = request.param

    yield web_driver
    web_driver.quit()

@pytest.fixture(scope='function')
def registration():
    helpers = Helpers()
    email, name, password = helpers.generate_data()
    payload = {
        "email": email,
        "password": password,
        "name": name,
            }
    response = requests.post(API.CREATE_USER, data=payload)
    token = response.json().get("accessToken")
    yield email, password
    requests.delete(API.DELETE_DATA, headers={"Authorization": f'{token}'})

@pytest.fixture(scope='function')
def log_in_and_create_order(registration):
    email, password = registration
    payload = {
        "email": email,
        "password": password,
            }
    response = requests.post(API.LOGIN_USER, data=payload)
    token = response.json().get("accessToken")
    payload = {
        "ingredients": [Ingredients.BUN_R2_D3, Ingredients.MAIN_PROTOSTOMIA, Ingredients.SAUSE_SPICY_X]
    }
    headers = {"Content-type": "application/json", "Authorization": f'{token}'}
    response = requests.post(API.CREATE_ORDER, headers=headers, json=payload)
    number = str(response.json()['order']['number'])
    return email, password, number


@pytest.fixture(scope='function')
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture(scope='function')
def recovery_page(driver):
    return RecoveryPage(driver)

@pytest.fixture(scope='function')
def main_page(driver):
    return MainPage(driver)

@pytest.fixture(scope='function')
def personal_page(driver):
    return PersonalPage(driver)

@pytest.fixture(scope='function')
def feed_page(driver):
    return FeedPage(driver)
