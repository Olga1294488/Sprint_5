import pytest
from browser import get_chrome_driver
from helpers import UserHelper
from urls import Urls


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
    from data import UserGenerator
    email = UserGenerator.generate_email()
    password = UserGenerator.generate_password(8)
    name = UserGenerator.generate_name()
    return user_helper.register_new_user(email, password, name)

@pytest.fixture
def logged_in_user(user_helper):
    """Фикстура: залогиненный пользователь"""
    from data import UserData
    user_helper.login_user(UserData.EXISTING_USER_EMAIL, UserData.EXISTING_USER_PASSWORD)
    return user_helper