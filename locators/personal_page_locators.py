from selenium.webdriver.common.by import By


class PersonalPageLocators:
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, ".//p[contains(@class, 'AppHeader_header__linkText') and text()='Личный Кабинет']"
    USER_HISTORY_MENU = By.XPATH, "//a[text()='История заказов']"
    LOG_OUT_MENU = By.XPATH, "//button[text()='Выход']"
    LOG_IN_BUTTON = By.XPATH, ".//button[text()='Войти']"
    NUMBER_ORDER_BLOCK = By.XPATH, "//p[contains(@class, 'text_type_digits')]"
    ORDER_WITH_NUMBER_ORDER_BLOCKS = By.XPATH, ".//div[contains(@class, 'OrderHistory_textBox')]/p[@class='text text_type_digits-default']"