import random
import string
import json
import os


def generate_random_string(length):
    """Генерация случайной строки"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def generate_unique_email():
    """Генерация уникального email для регистрации"""
    import time
    # Используем timestamp для гарантии уникальности
    timestamp = int(time.time())
    return f"test_user_{timestamp}@yandex.ru"


def load_test_user():
    """Загрузка данных тестового пользователя из файла"""
    try:
        with open("test_user.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None


class TestData:
    # Тестовые данные
    BASE_URL = "https://stellarburgers.education-services.ru/"
    
    # Загружаем данные пользователя из файла, если есть
    _test_user = load_test_user()
    
    if _test_user:
        EXISTING_USER_EMAIL = _test_user["email"]
        EXISTING_USER_PASSWORD = _test_user["password"]
        EXISTING_USER_NAME = _test_user["name"]
    else:
        BASE_URL = "https://stellarburgers.education-services.ru/"
        EXISTING_USER_EMAIL = "test_user_1773668569@yandex.ru"
        EXISTING_USER_PASSWORD = "qikvsfnj"
        EXISTING_USER_NAME = "Test User"  
    # Пароли для тестирования регистрации
    VALID_PASSWORD = generate_random_string(6)
    INVALID_PASSWORD = generate_random_string(5)
