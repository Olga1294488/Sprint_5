import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators, ForgotPasswordPageLocators
from data import Urls, UserData, ExpectedTexts


class TestLogin:
    """Тесты для входа в систему"""
    
    def login_user(self, driver, email, password):
        """Вспомогательный метод для входа"""
        driver.get(Urls.BASE_URL)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON)
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(email)
        
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    
    def test_login_main_page_button(self, driver):
        """Вход через кнопку 'Войти в аккаунт' на главной"""
        self.login_user(driver, UserData.EXISTING_USER_EMAIL, UserData.EXISTING_USER_PASSWORD)
        
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        ).is_displayed()
    
    def test_login_personal_account_button(self, driver):
        """Вход через кнопку 'Личный кабинет'"""
        driver.get(Urls.BASE_URL)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(UserData.EXISTING_USER_EMAIL)
        
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(UserData.EXISTING_USER_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        ).is_displayed()
    
    def test_login_registration_form(self, driver):
        """Вход через кнопку в форме регистрации"""
        driver.get(Urls.BASE_URL)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON)
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_LINK)
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(UserData.EXISTING_USER_EMAIL)
        
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(UserData.EXISTING_USER_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        ).is_displayed()
    
    def test_login_forgot_password_form(self, driver):
        """Вход через кнопку в форме восстановления пароля"""
        driver.get(Urls.BASE_URL)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON)
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.FORGOT_PASSWORD_LINK)
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ForgotPasswordPageLocators.LOGIN_LINK)
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(UserData.EXISTING_USER_EMAIL)
        
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(UserData.EXISTING_USER_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        ).is_displayed()