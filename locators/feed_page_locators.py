from selenium.webdriver.common.by import By

class FeedPageLocators:

    ORDER_FEED_BUTTON = By.XPATH, "//p[text()='Лента Заказов']"
    HEADER_ORDER_FEED = By.XPATH, "//h1[text()='Лента заказов']"
    ORDER_BLOCK = By.XPATH, "//a[@class='OrderHistory_link__1iNby']"
    ORDER_BLOCK_POP_UP = By.XPATH, "//div[contains(@class, 'Modal_orderBox')]"
    NUMBER_ORDER_BLOCK = By.XPATH, "//p[contains(@class, 'text_type_digits')]"
    COUNTER_ALL_TIME = By.XPATH, "//p[contains(@class, 'text_type_digits-large')]"
    ORDER_WITH_NUMBER_ORDER_BLOCKS = By.XPATH, ".//div[contains(@class, 'OrderHistory_textBox')]/p[@class='text text_type_digits-default']"
    COUNTER_DAY = By.XPATH, "//p[contains(@class, 'text_type_main') and contains(text(), 'Выполнено за сегодня')]/following-sibling::p[contains(@class, 'text_type_digits-large')]"
    NUMBER_ORDER_LIST_ONLINE = By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]//li[contains(@class, 'text_type_digits-default')]"
