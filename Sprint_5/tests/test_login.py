from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import (
    MainPageLocators, LoginPageLocators, RegistrationPageLocators,
    ForgotPasswordPageLocators, ProfilePageLocators
)
from data import TestData


class TestLogin:
    
    def test_login_main_page_button(self, driver):
        """Вход через кнопку 'Войти в аккаунт' на главной"""
        driver.get(TestData.BASE_URL)
        
        # Клик по кнопке "Войти в аккаунт"
        driver.find_element(*MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
        
        # Вход в систему
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TestData.EXISTING_USER_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TestData.EXISTING_USER_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Проверка успешного входа (появление кнопки "Оформить заказ")
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        assert driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).is_displayed()
    
    def test_login_personal_account_button(self, driver):
        """Вход через кнопку 'Личный кабинет'"""
        driver.get(TestData.BASE_URL)
        
        # Клик по кнопке "Личный кабинет"
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        # Вход в систему
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TestData.EXISTING_USER_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TestData.EXISTING_USER_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Проверка успешного входа
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        assert driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).is_displayed()
    
    def test_login_registration_form(self, driver):
        """Вход через кнопку в форме регистрации"""
        driver.get(TestData.BASE_URL)
        
        # Переход на страницу регистрации
        driver.find_element(*MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
        
        # Клик по ссылке "Войти" на странице регистрации
        driver.find_element(*RegistrationPageLocators.LOGIN_LINK).click()
        
        # Вход в систему
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TestData.EXISTING_USER_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TestData.EXISTING_USER_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Проверка успешного входа
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        assert driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).is_displayed()
    
    def test_login_forgot_password_form(self, driver):
        """Вход через кнопку в форме восстановления пароля"""
        driver.get(TestData.BASE_URL)
        
        # Переход на страницу восстановления пароля
        driver.find_element(*MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*LoginPageLocators.FORGOT_PASSWORD_LINK).click()
        
        # Клик по ссылке "Войти" на странице восстановления пароля
        driver.find_element(*ForgotPasswordPageLocators.LOGIN_LINK).click()
        
        # Вход в систему
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TestData.EXISTING_USER_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TestData.EXISTING_USER_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Проверка успешного входа
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        assert driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).is_displayed()
