import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators, LoginPageLocators, ProfilePageLocators
from data import Urls, UserData


class TestProfile:
    """Тесты для личного кабинета"""
    
    def login(self, driver):
        """Вход в систему"""
        driver.get(Urls.BASE_URL)
        
        # Клик по кнопке "Войти в аккаунт" на главной
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON)
        ).click()
        
        # Заполнение формы логина
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(UserData.EXISTING_USER_EMAIL)
        
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(UserData.EXISTING_USER_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Проверка успешного входа - видна кнопка "Оформить заказ"
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        ).is_displayed()
    
    def test_go_to_personal_account(self, driver):
        """Переход в личный кабинет"""
        self.login(driver)
        
        # Клик по кнопке "Личный кабинет"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        # Проверка, что мы в профиле
        assert WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(ProfilePageLocators.PROFILE_LINK)
        )
        assert "profile" in driver.current_url or "account" in driver.current_url
    
    def test_go_to_constructor_from_profile(self, driver):
        """Переход из личного кабинета в конструктор"""
        self.login(driver)
        
        # Переход в профиль
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        # Ждем загрузки профиля
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(ProfilePageLocators.PROFILE_LINK)
        )
        
        # Клик по конструктору
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
        ).click()
        
        # Проверка, что мы на главной
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        ).is_displayed()
    
    def test_go_to_main_from_profile_by_logo(self, driver):
        """Переход из личного кабинета на главную по клику на логотип"""
        self.login(driver)
        
        # Переход в профиль
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        # Ждем загрузки профиля
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(ProfilePageLocators.PROFILE_LINK)
        )
        
        # Клик по логотипу
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGO)
        ).click()
        
        # Проверка, что мы на главной
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        ).is_displayed()
    
    def test_logout(self, driver):
        """Выход из аккаунта"""
        self.login(driver)
        
        # Переход в профиль
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        # Ждем загрузки профиля
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(ProfilePageLocators.PROFILE_LINK)
        )
        
        # Клик по кнопке выхода
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)
        ).click()
        
               
        # Альтернативный вариант проверки:
        assert WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
).is_displayed()