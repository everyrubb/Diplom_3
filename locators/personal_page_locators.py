from selenium.webdriver.common.by import By


class PersonalPageLocators:
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, ".//p[contains(@class, 'AppHeader_header__linkText') and text()='Личный Кабинет']"
    USER_HISTORY_MENU = By.XPATH, "//a[text()='История заказов']"
    LOG_OUT_MENU = By.XPATH, "//button[text()='Выход']"