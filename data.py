import random
import string
import time


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def generate_unique_email():
    timestamp = int(time.time())
    return f"test_user_{timestamp}@yandex.ru"


class Urls:
    BASE_URL = "https://stellarburgers.education-services.ru/"


class UserData:
    EXISTING_USER_EMAIL = "test_user_1773757128@yandex.ru"
    EXISTING_USER_PASSWORD = "ikqeryzk"
    EXISTING_USER_NAME = "Test User"


class RegistrationData:
    @staticmethod
    def get_valid_password():
        return generate_random_string(6)
    
    @staticmethod
    def get_invalid_password():
        return generate_random_string(5)


class UserGenerator:
    @staticmethod
    def generate_email():
        return generate_unique_email()
    
    @staticmethod
    def generate_name():
        names = ["Test User", "New User", "Auto Test", "QA Tester"]
        return random.choice(names)
    
    @staticmethod
    def generate_password(length=8):
        return generate_random_string(length)


class ExpectedTexts:
    BUNS_SECTION = "Булки"
    SAUCES_SECTION = "Соусы"
    FILLINGS_SECTION = "Начинки"
    
    LOGIN_BUTTON_TEXT = "Войти"
    REGISTER_BUTTON_TEXT = "Зарегистрироваться"
    LOGOUT_BUTTON_TEXT = "Выход"
    ORDER_BUTTON_TEXT = "Оформить заказ"
    PERSONAL_ACCOUNT_TEXT = "Личный Кабинет"
    
    PROFILE_LINK_TEXT = "Профиль"
    ORDER_HISTORY_TEXT = "История заказов"
    CONSTRUCTOR_TEXT = "Конструктор"
    
    INCORRECT_PASSWORD_ERROR = "Некорректный пароль"