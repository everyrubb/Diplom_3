import allure

from const import Const
from locators.feed_page_locators import FeedPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Открыть главную страницу Stellar Burgers")
    def open_main_page(self):
        self.open_url(Const.MAIN_PAGE)
        self.wait_element_visibility_of_element_located(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Открыть страницу авторизации")
    def open_login_account(self):
        self.open_url(Const.MAIN_PAGE)
        self.click_on_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.wait_element_visibility_of_element_located(LoginPageLocators.HEADER_LOGIN_PAGE)

    @allure.step("Открыть страницу Конструктора")
    def open_constructor(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        return self.find_element(MainPageLocators.HEADER_CONSTRUCTOR)

    @allure.step("Открыть ленту заказа")
    def open_order_feed(self):
        self.click_on_element(FeedPageLocators.ORDER_FEED_BUTTON)
        self.wait_element_visibility_of_element_located(FeedPageLocators.HEADER_ORDER_FEED)
        self.find_element(FeedPageLocators.HEADER_ORDER_FEED)
        return self.get_current_url()

    @allure.step("Открыть всплывающее окно «Детали ингредиента»")
    def open_ingredient_pop_up(self):
        self.click_on_element(MainPageLocators.BUN_ITEM)
        self.wait_element_visibility_of_element_located(MainPageLocators.HEADER_POP_UP)
        return self.find_element(MainPageLocators.HEADER_POP_UP)

    @allure.step("Открыть всплывающее окно «Детали ингредиента»")
    def close_ingredient_pop_up(self):
        self.click_on_element(MainPageLocators.CLOSE_POP_UP_BUTTON)
        self.wait_element_visibility_of_element_located(MainPageLocators.BUN_ITEM)
        return self.find_element(MainPageLocators.CLOSE_POP_UP)

    @allure.step("Добавить ингредиент в заказ")
    def add_items_in_order(self):
        self.wait_element_visibility_of_element_located(MainPageLocators.COUNTER_BUN)
        counter = self.get_text(MainPageLocators.COUNTER_BUN)
        self.drag_drop(MainPageLocators.BUN_ITEM, MainPageLocators.ADD_SECTION)
        return counter

    @allure.step("Проверить изменение счетчика ингредиента")
    def check_counter_after_add(self):
        counter = self.get_text(MainPageLocators.COUNTER_BUN)
        return counter

    @allure.step("Тапнуть на кнопку «Оформить заказ")
    def tap_button_create_order(self):
        self.wait_element_visibility_of_element_located(MainPageLocators.CREATE_ORDER_BUTTON)
        self.click_on_element(MainPageLocators.CREATE_ORDER_BUTTON)
        self.wait_element_visibility_of_element_located(MainPageLocators.CREATE_ORDER_POP_UP)
        return self.find_element(MainPageLocators.HEADER_CREATE_ORDER_POP_UP)

    @allure.step("Оформить заказ")
    def create_order(self):
        self.open_main_page()
        self.add_items_in_order()
        self.tap_button_create_order()
