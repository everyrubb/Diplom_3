from time import sleep

import allure
from locators.feed_page_locators import FeedPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.personal_page_locators import PersonalPageLocators
from pages.base_page import BasePage


class PersonalPage(BasePage):

    @allure.step("Открыть персональную страницу")
    def open_personal_page(self):
        if self.driver.browser_name == "firefox":
            sleep(1)
        self.wait_element_visibility_of_element_located(PersonalPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_on_element(PersonalPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Открыть историю заказов через меню личного кабинета")
    def open_history_orders(self):
        if self.driver.browser_name == "firefox":
            sleep(1)
        self.wait_element_visibility_of_element_located(PersonalPageLocators.USER_HISTORY_MENU)
        self.click_on_element(PersonalPageLocators.USER_HISTORY_MENU)
        return self.get_current_url()

    def find_number_order_in_history_orders(self):
        self.wait_element_visibility_of_element_located(FeedPageLocators.ORDER_WITH_NUMBER_ORDER_BLOCKS)
        number_in_history = self.get_text(FeedPageLocators.NUMBER_ORDER_BLOCK)
        clean_number_in_history = number_in_history.lstrip('#0')
        return clean_number_in_history

    @allure.step("Выйти из аккаунта")
    def log_out_in_pesonal_account(self):
        if self.driver.browser_name == "firefox":
            sleep(1)
        self.wait_element_visibility_of_element_located(PersonalPageLocators.LOG_OUT_MENU)
        self.click_on_element(PersonalPageLocators.LOG_OUT_MENU)
        self.wait_element_visibility_of_element_located(LoginPageLocators.LOG_IN_BUTTON)
        return self.get_current_url()

    @allure.step("Проверяем наличие заказа на странице «История заказов»")
    def check_order_in_history_orders(self, number):
        all_orders = self.wait_element_presence_of_all_elements_located(FeedPageLocators.ORDER_WIRH_NUMBER_ORDER_BLOCKS)
        self.find_element(all_orders)
        for order in all_orders:
            if number in order.text:
                return True
            else:
                return False
