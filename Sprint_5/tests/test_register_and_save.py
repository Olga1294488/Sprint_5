import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators, LoginPageLocators
from data import Urls, UserGenerator


class TestRegisterAndSave:
    """Тесты регистрации с сохранением данных"""
    
    @pytest.fixture
    def generated_user_data(self):
        """Фикстура для генерации данных пользователя"""
        return {
            "email": UserGenerator.generate_email(),
            "password": UserGenerator.generate_password(8),
            "name": UserGenerator.generate_name()
        }
    
    def test_user_data_not_none(self, driver, user_helper, generated_user_data):
        """Тест 1: Проверка, что пользователь создан (не None)"""
        data = generated_user_data
        user_data = user_helper.register_new_user(
            data["email"], 
            data["password"], 
            data["name"]
        )
        assert user_data is not None
    
    def test_user_data_has_email(self, driver, user_helper, generated_user_data):
        """Тест 2: Проверка наличия email в данных пользователя"""
        data = generated_user_data
        user_data = user_helper.register_new_user(
            data["email"], 
            data["password"], 
            data["name"]
        )
        assert "email" in user_data
    
    def test_user_data_has_password(self, driver, user_helper, generated_user_data):
        """Тест 3: Проверка наличия пароля в данных пользователя"""
        data = generated_user_data
        user_data = user_helper.register_new_user(
            data["email"], 
            data["password"], 
            data["name"]
        )
        assert "password" in user_data
    
    def test_user_data_has_name(self, driver, user_helper, generated_user_data):
        """Тест 4: Проверка наличия имени в данных пользователя"""
        data = generated_user_data
        user_data = user_helper.register_new_user(
            data["email"], 
            data["password"], 
            data["name"]
        )
        assert "name" in user_data
    
    def test_can_login_with_new_user(self, driver, user_helper, generated_user_data):
        """Тест 5: Проверка возможности входа с новым пользователем"""
        data = generated_user_data
        user_data = user_helper.register_new_user(
            data["email"], 
            data["password"], 
            data["name"]
        )
        
        driver.get(Urls.BASE_URL)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON)
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(user_data["email"])
        
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user_data["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        ).is_displayed()