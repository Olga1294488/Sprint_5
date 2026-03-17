import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators
from data import Urls, UserGenerator, RegistrationData


class TestRegisterAndSave:
    """Тесты регистрации с сохранением данных"""
    
    def test_register_new_user(self, driver, user_helper):
        """Регистрация нового пользователя через хелпер"""
        
        # Используем хелпер для регистрации
        user_data = user_helper.register_new_user()
        
        # Проверяем, что пользователь создан
        assert user_data is not None
        assert "email" in user_data
        assert "password" in user_data
        assert "name" in user_data
        
        # Проверяем, что можно войти с новым пользователем
        driver.get(Urls.BASE_URL)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON)
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(user_data["email"])
        
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user_data["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Проверяем успешный вход
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        ).is_displayed()