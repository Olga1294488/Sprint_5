"""Модуль с URL-адресами приложения"""


class Urls:
    """Класс с URL-адресами приложения"""
    BASE_URL = "https://stellarburgers.education-services.ru/"
    LOGIN_URL = f"{BASE_URL}login"
    REGISTER_URL = f"{BASE_URL}register"
    FORGOT_PASSWORD_URL = f"{BASE_URL}forgot-password"
    PROFILE_URL = f"{BASE_URL}profile"
    ORDER_FEED_URL = f"{BASE_URL}feed"