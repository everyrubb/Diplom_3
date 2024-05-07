import allure
from const import Const

class TestPersonalAccount:

    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    @allure.description('Проверяем, что при тапе на «Личный кабинет» пользователь переходит на страницу аккаунта')
    def test_check_enter_to_personal_account_in_main_page(self, main_page):
        main_page.open_login_account()
        assert main_page.get_current_url() == Const.LOGIN_PAGE

    @allure.title('Проверка перехода в раздел «История заказов»')
    @allure.description('Проверяем, что при тапе на «История заказов» пользователь переходит на страницу истории заказов')
    def test_check_open_history_orders_in_personal_page(self, registration, login_page, personal_page):
        login_page.open_login_page()
        login_page.log_in(registration)
        personal_page.open_personal_page()
        assert personal_page.open_history_orders() == Const.HISTORY_PAGE

    @allure.title('Проверка выход из аккаунта')
    @allure.description('Проверяем, что при тапе на «Выход» пользователь выходит из аккаунта')
    def test_check_log_out_account_in_personal_page(self, registration, personal_page, login_page):
        login_page.open_login_page()
        login_page.log_in(registration)
        personal_page.open_personal_page()
        assert personal_page.log_out_in_pesonal_account() == Const.LOGIN_PAGE
