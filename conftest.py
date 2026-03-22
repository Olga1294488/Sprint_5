import pytest
from browser import get_chrome_driver
from helpers import UserHelper


@pytest.fixture
def driver():
    """Фикстура для браузера Chrome"""
    driver = get_chrome_driver()
    yield driver
    driver.quit()


@pytest.fixture
def user_helper(driver):
    """Фикстура для работы с пользователями"""
    return UserHelper(driver)


@pytest.fixture
def registered_user(user_helper):
    """Фикстура, создающая зарегистрированного пользователя"""
    return user_helper.register_new_user()