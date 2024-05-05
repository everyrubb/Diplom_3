class Const:

    MAIN_PAGE = 'https://stellarburgers.nomoreparties.site'
    LOGIN_PAGE = 'https://stellarburgers.nomoreparties.site/login'
    RECOVERY_PAGE = 'https://stellarburgers.nomoreparties.site/forgot-password'
    RESET_PASSWORD = 'https://stellarburgers.nomoreparties.site/reset-password'
    PROFILE_PAGE = 'https://stellarburgers.nomoreparties.site/account/profile'
    HISTORY_PAGE = 'https://stellarburgers.nomoreparties.site/account/order-history'
    FEED_PAGE = 'https://stellarburgers.nomoreparties.site/feed'

class API:
    MAIN_PAGE = 'https://stellarburgers.nomoreparties.site'
    CREATE_USER = f'{MAIN_PAGE}/api/auth/register'
    LOGIN_USER = f'{MAIN_PAGE}/api/auth/login'
    CREATE_ORDER = f'{MAIN_PAGE}/api/orders'
    DELETE_DATA = f'{MAIN_PAGE}/api/auth/user'


class Ingredients:
    BUN_R2_D3 = '61c0c5a71d1f82001bdaaa6d'
    MAIN_PROTOSTOMIA = '61c0c5a71d1f82001bdaaa6f'
    SAUSE_SPICY_X = '61c0c5a71d1f82001bdaaa72'