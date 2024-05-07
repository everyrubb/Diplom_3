from selenium.webdriver.common.by import By


class LoginPageLocators:

    LOG_IN_BUTTON = By.XPATH, ".//button[text()='Войти']"
    RECOVERY_BUTTON = By.XPATH, "//a[text()='Восстановить пароль']"
    HEADER_LOGIN_PAGE = By.XPATH, "//h2[text()='Вход']"
    PASSWORD_INPUT = By.XPATH, "//label[text()='Пароль']/../input"
    EMAIL_INPUT = By.XPATH, "//label[text()='Email']/../input"
    CREATE_ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']"