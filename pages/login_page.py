import allure

from const import Const
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage

class LoginPage(BasePage):

    @allure.step("Открыть страницу авторизации")
    def open_login_page(self):
        self.open_url(Const.LOGIN_PAGE)
        self.wait_element_visibility_of_element_located(LoginPageLocators.LOG_IN_BUTTON)

    @allure.step("Тапнуть на кнопку «Восстановить пароль»")
    def click_recovery_button(self):
        self.click_on_element(LoginPageLocators.RECOVERY_BUTTON)

    @allure.step("Авторизоваться новым пользователем без заказа")
    def log_in(self, registration):
        email, password = registration
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)
        self.click_on_element(LoginPageLocators.LOG_IN_BUTTON)
        self.wait_element_presence_of_element_located(LoginPageLocators.CREATE_ORDER_BUTTON)

    @allure.step("Авторизоваться")
    def log_in_main_page(self, registration):
        self.open_login_page()
        self.log_in(registration)

    @allure.step("Авторизоваться пользователем с заказом заказа")
    def log_in_with_order(self, log_in_and_create_order):
        email, password, number = log_in_and_create_order
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)
        self.wait_element_presence_of_element_located(LoginPageLocators.LOG_IN_BUTTON)
        self.click_on_element(LoginPageLocators.LOG_IN_BUTTON)
        return number
