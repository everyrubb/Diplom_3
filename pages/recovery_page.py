import allure

from const import Const
from locators.recovery_page_locators import RecoveryPageLocators
from pages.base_page import BasePage

class RecoveryPage(BasePage):

    @allure.step("Открыть страницу восстановления пароля")
    def open_recovery_page(self):
        self.open_url(Const.RECOVERY_PAGE)
        self.wait_element_visibility_of_element_located(RecoveryPageLocators.HEADER_RECOVERY_PAGE)

    @allure.step("Ввести электронную почту на странице восстановления пароля")
    def set_email_in_input(self, registration):
        email, _ = registration
        self.send_keys(RecoveryPageLocators.EMAIL_INPUT, email)

    @allure.step("Тапнуть на кнопку «Восстановить» на странице восстановления пароля")
    def click_recovery_button(self):
        self.click_on_element(RecoveryPageLocators.RECOVERY_BUTTON)
        self.wait_element_visibility_of_element_located(RecoveryPageLocators.SAVE_BUTTON)

    @allure.step("Ввести пароль на странице восстановления пароля")
    def set_password_in_input(self, registration):
        email, _ = registration
        self.send_keys(RecoveryPageLocators.PASSWORD_INPUT, email)

    def open_reset_password(self, registration):
        self.open_recovery_page()
        self.set_email_in_input(registration)
        self.click_recovery_button()
        self.set_password_in_input(registration)

    @allure.step("Тапнуть на иконку глазика для открытия пароля")
    def click_on_eye_icon(self):
        self.click_on_element(RecoveryPageLocators.EYE_BUTTON)
        return self.find_element(RecoveryPageLocators.PASSWORD_INPUT_ACTIVE)
