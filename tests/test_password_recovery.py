import allure

from const import Const

class TestRecoveryPassword:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @allure.description('Проверяем, что при нажатии на кнопку  «Восстановить пароль» пользователь переходит на страницу')
    def test_check_open_recovery_page_on_button(self, login_page):
        login_page.open_login_page()
        login_page.click_recovery_button()
        assert login_page.get_current_url() == Const.RECOVERY_PAGE

    @allure.title('Проверка ввода почты и клика по кнопке «Восстановить»')
    @allure.description('Проверяем, что при вводе почты и клика по кнопке «Восстановить» открывается страница ввода пароля')
    def test_enter_email_and_click_recovery_button(self, recovery_page, registration):
        recovery_page.open_recovery_page()
        recovery_page.set_email_in_input(registration)
        recovery_page.click_recovery_button()
        assert recovery_page.get_current_url() == Const.RESET_PASSWORD

    @allure.title('Проверка тапа на показ/сокрытие пароля в поле «Пароль»')
    @allure.description('Проверяем, при тапе на значок делает поле активным — подсвечивает его')
    def test_check_active_email_input_after_click_eye_icon(self, recovery_page, registration):
        recovery_page.open_reset_password(registration)
        assert recovery_page.click_on_eye_icon()
