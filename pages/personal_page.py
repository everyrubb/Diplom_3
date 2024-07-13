import allure

from locators.personal_page_locators import PersonalPageLocators
from pages.base_page import BasePage


class PersonalPage(BasePage):

    @allure.step("Открыть персональную страницу")
    def open_personal_page(self):
        self.wait_element_visibility_of_element_located(PersonalPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_on_element(PersonalPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Открыть историю заказов через меню личного кабинета")
    def open_history_orders(self):
        self.wait_element_visibility_of_element_located(PersonalPageLocators.USER_HISTORY_MENU)
        self.click_on_element(PersonalPageLocators.USER_HISTORY_MENU)
        return self.get_current_url()

    @allure.step("Найти номер заказа в истории заказов")
    def find_number_order_in_history_orders(self):
        self.wait_element_visibility_of_element_located(PersonalPageLocators.ORDER_WITH_NUMBER_ORDER_BLOCKS)
        number_in_history = self.get_text(PersonalPageLocators.NUMBER_ORDER_BLOCK)
        clean_number_in_history = number_in_history.lstrip('#0')
        return clean_number_in_history

    @allure.step("Выйти из аккаунта")
    def log_out_in_pesonal_account(self):
        self.wait_element_visibility_of_element_located(PersonalPageLocators.LOG_OUT_MENU)
        self.click_on_element(PersonalPageLocators.LOG_OUT_MENU)
        self.wait_element_visibility_of_element_located(PersonalPageLocators.LOG_IN_BUTTON)
        return self.get_current_url()
