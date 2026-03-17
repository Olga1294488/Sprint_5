import random
import string


def generate_random_string(length):
    """Генерация случайной строки"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def generate_unique_email():
    """Генерация уникального email для регистрации"""
    import time
    timestamp = int(time.time())
    return f"test_user_{timestamp}@yandex.ru"


class Urls:
    """Класс с URL-адресами приложения"""
    BASE_URL = "https://stellarburgers.education-services.ru/"


class UserData:
    """Класс с данными существующего пользователя для тестов входа"""
    # ВАЖНО: Это должен быть реальный существующий пользователь!
    EXISTING_USER_EMAIL = "test_user_1773757128@yandex.ru"
    EXISTING_USER_PASSWORD = "ikqeryzk"
    EXISTING_USER_NAME = "Test User"


class RegistrationData:
    """Класс с данными для тестов регистрации"""
    
    @staticmethod
    def get_valid_password():
        """Возвращает валидный пароль (6+ символов)"""
        return generate_random_string(6)
    
    @staticmethod
    def get_invalid_password():
        """Возвращает невалидный пароль (менее 6 символов)"""
        return generate_random_string(5)


class UserGenerator:
    """Класс для генерации новых пользователей"""
    
    @staticmethod
    def generate_email():
        """Генерация уникального email"""
        return generate_unique_email()
    
    @staticmethod
    def generate_name():
        """Генерация имени пользователя"""
        names = ["Test User", "New User", "Auto Test", "QA Tester"]
        return random.choice(names)
    
    @staticmethod
    def generate_password(length=8):
        """Генерация пароля указанной длины"""
        return generate_random_string(length)


class ExpectedTexts:
    """Класс с ожидаемыми текстами элементов интерфейса"""
    
    # Заголовки разделов конструктора
    BUNS_SECTION = "Булки"
    SAUCES_SECTION = "Соусы"
    FILLINGS_SECTION = "Начинки"
    
    # Тексты кнопок
    LOGIN_BUTTON_TEXT = "Войти"
    REGISTER_BUTTON_TEXT = "Зарегистрироваться"
    LOGOUT_BUTTON_TEXT = "Выход"
    ORDER_BUTTON_TEXT = "Оформить заказ"
    PERSONAL_ACCOUNT_TEXT = "Личный Кабинет"
    
    # Тексты ссылок
    PROFILE_LINK_TEXT = "Профиль"
    ORDER_HISTORY_TEXT = "История заказов"
    CONSTRUCTOR_TEXT = "Конструктор"
    
    # Сообщения об ошибках
    INCORRECT_PASSWORD_ERROR = "Некорректный пароль"