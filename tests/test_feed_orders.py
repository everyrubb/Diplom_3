import allure

class TestFeedOrdersPage:

    @allure.title('Проверка перехода к деталям заказа по клику на заказ в Ленте заказов')
    @allure.description('Проверяем, что при тапе заказ открывается окно с деталями заказа')
    def test_check_open_order_details(self, feed_page):
        feed_page.open_feed_page()
        assert feed_page.click_on_order_block()

    @allure.title('Синхронизация раздела «История заказов» со страницей «Лента заказов»')
    @allure.description('Проверяем, что заказы из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_check_sync_history_order_and_feed_orders(self, feed_page, log_in_and_create_order, login_page, personal_page):
        login_page.open_login_page()
        number = login_page.log_in_with_order(log_in_and_create_order)
        personal_page.open_personal_page()
        personal_page.open_history_orders()
        number_in_history = personal_page.find_number_order_in_history_orders()
        feed_page.open_feed_page()
        number_in_feed = feed_page.check_number_order_in_feed_page(number)
        assert number == number_in_history and number_in_feed == True

    @allure.title('Проверка увеличения счетчика «Выполнено за всё время» после создания заказа')
    @allure.description('Проверяем, что счетчик «Выполнено за все время» увеличивается на странице «Лента заказов»')
    def test_check_rise_counter_all_time_after_made_order(self, feed_page, login_page, main_page, registration):
        feed_page.open_feed_page()
        counter_before = feed_page.check_counter_all_time()
        login_page.log_in_main_page(registration)
        main_page.create_order()
        feed_page.open_feed_page()
        counter_after = feed_page.check_counter_all_time()
        assert counter_before != counter_after

    @allure.title('Проверка увеличения счетчика «Выполнено за сегодня» после создания заказа')
    @allure.description('Проверяем, что счетчик «Выполнено за сегодня» увеличивается на странице «Лента заказов»')
    def test_check_rise_counter_day_after_made_order(self, feed_page, login_page, main_page, registration):
        feed_page.open_feed_page()
        counter_before = feed_page.check_counter_day()
        login_page.log_in_main_page(registration)
        main_page.create_order()
        feed_page.open_feed_page()
        counter_after = feed_page.check_counter_day()
        assert counter_before != counter_after

    @allure.title('Проверка увеличения счетчика «В работе» после создания заказа')
    @allure.description('Проверяем, что счетчик «Выполнено за сегодня» увеличивается на странице «Лента заказов»')
    def test_check_rise_counter_at_work_after_made_order(self, feed_page, login_page, personal_page, main_page, registration, log_in_and_create_order):
        login_page.open_login_page()
        number = login_page.log_in_with_order(log_in_and_create_order)
        feed_page.open_feed_page()
        number_in_at_work = feed_page.check_number_order_in_at_work()
        assert number == number_in_at_work
