import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators, LoginPageLocators, ErrorMessages
from data import Urls, UserGenerator


class TestRegisterAndSave:
    """Тесты регистрации с сохранением данных"""
    
    @pytest.fixture
    def new_user_data(self):
        """Фикстура: генерирует данные нового пользователя"""
        return {
            "email": UserGenerator.generate_email(),
            "password": UserGenerator.generate_password(8),
            "name": UserGenerator.generate_name()
        }
    
    def test_successful_registration_shows_login_page(self, driver, user_helper, new_user_data):
        """
        Тест 1: Проверка, что после успешной регистрации
        появляется страница входа (кнопка "Войти")
        """
        email = new_user_data["email"]
        password = new_user_data["password"]
        name = new_user_data["name"]
        
        # Регистрируем пользователя
        user_helper.register_new_user(email, password, name)
        
        # Проверяем, что появилась страница входа
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        ).is_displayed()
    
    def test_registered_user_can_login(self, driver, user_helper, new_user_data):
        """
        Тест 2: Проверка, что зарегистрированный пользователь
        может войти в систему
        """
        email = new_user_data["email"]
        password = new_user_data["password"]
        name = new_user_data["name"]
        
        # Регистрируем пользователя
        user_helper.register_new_user(email, password, name)
        
        # Выходим на главную (после регистрации мы на странице входа)
        driver.get(Urls.BASE_URL)
        
        # Входим с новым пользователем
        user_helper.login_user(email, password)
        
        # Проверяем, что вход выполнен (появилась кнопка "Оформить заказ")
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        ).is_displayed()
    
    def test_registration_with_existing_email_shows_error(self, driver, user_helper, new_user_data):
        """
        Тест 3: Проверка, что регистрация с уже существующим email
        показывает ошибку
        """
        email = new_user_data["email"]
        password = new_user_data["password"]
        name = new_user_data["name"]
        
        # Первая регистрация - успешная
        user_helper.register_new_user(email, password, name)
        
        # Возвращаемся на главную
        driver.get(Urls.BASE_URL)
        
        # Пытаемся зарегистрироваться с тем же email
        user_helper.go_to_registration_page()
        user_helper.fill_registration_form(name, email, password)
        
        # Проверяем, что появилось сообщение об ошибке
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ErrorMessages.USER_ALREADY_EXISTS)
        ).is_displayed()