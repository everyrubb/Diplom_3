import allure

from const import Const

class TestMadeOrderMainPage:

    @allure.title('Проверка перехода по клику на «Конструктор»')
    @allure.description('Проверяем, что при тапе на «Конструктор» пользователь переходит в конструктор')
    def test_check_open_constructor(self, main_page, login_page):
        login_page.open_login_page()
        assert main_page.open_constructor()

    @allure.title('Проверка перехода по клику на «Лента заказов»')
    @allure.description('Проверяем, что при тапе на «Лента заказов» пользователь переходит в ленту')
    def test_check_open_order_feed(self, main_page):
        main_page.open_main_page()
        assert main_page.open_order_feed() == Const.FEED_PAGE

    @allure.title('Проверка открытия информации об ингредиенте»')
    @allure.description('Проверяем, что при тапе на «Лента заказов» пользователь переходит в ленту')
    def test_open_pop_up_about_ingredient(self, main_page):
        main_page.open_main_page()
        assert main_page.open_ingredient_pop_up()

    @allure.title('Проверка закрытия всплывающего окна «Детали ингредиента»')
    @allure.description('Проверяем, что при тапе на крестик всплывающее окно закрывается')
    def test_close_pop_up_about_ingredient(self, main_page):
        main_page.open_main_page()
        main_page.open_ingredient_pop_up()
        assert main_page.close_ingredient_pop_up()

    @allure.title('Проверка работа счетчика ингредиента после добавления самого ингредиента в заказ')
    @allure.description('Проверяем, что при переносе ингредиента в заказ его счетчик увеличивается')
    def test_check_counter_up_after_add_item_in_order(self, main_page):
        main_page.open_main_page()
        before = main_page.add_items_in_order()
        after = main_page.check_counter_after_add()
        assert before == '0'and after == '2'

    @allure.title('Проверка оформления заказа авторизованным пользователем')
    @allure.description('Проверяем, что авторизованный пользователь может сделать заказ')
    def test_check_create_order_authorized_user(self, registration, login_page, main_page):
        login_page.open_login_page()
        login_page.log_in(registration)
        main_page.add_items_in_order()
        assert main_page.tap_button_create_order()
