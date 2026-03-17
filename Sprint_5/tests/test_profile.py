import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators, LoginPageLocators, ProfilePageLocators
from data import Urls, UserData, ExpectedTexts


class TestProfile:
    """Тесты для личного кабинета"""
    
    def login(self, driver):
        """Вход в систему"""
        driver.get(Urls.BASE_URL)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON)
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(UserData.EXISTING_USER_EMAIL)
        
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(UserData.EXISTING_USER_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Проверка успешного входа
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//button[text()='{ExpectedTexts.ORDER_BUTTON_TEXT}']"))
        ).is_displayed()
    
    def test_go_to_personal_account(self, driver):
        """Переход в личный кабинет"""
        self.login(driver)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        

        assert WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//a[text()='{ExpectedTexts.PROFILE_LINK_TEXT}']"))
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
            EC.presence_of_element_located((By.XPATH, f"//a[text()='{ExpectedTexts.PROFILE_LINK_TEXT}']"))
        )
        
        # Клик по конструктору
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
        ).click()
        

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//button[text()='{ExpectedTexts.ORDER_BUTTON_TEXT}']"))
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
            EC.presence_of_element_located((By.XPATH, f"//a[text()='{ExpectedTexts.PROFILE_LINK_TEXT}']"))
        )
        
        # Клик по логотипу
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGO)
        ).click()
        

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//button[text()='{ExpectedTexts.ORDER_BUTTON_TEXT}']"))
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
            EC.presence_of_element_located((By.XPATH, f"//a[text()='{ExpectedTexts.PROFILE_LINK_TEXT}']"))
        )
        
        # Клик по кнопке выхода
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//button[text()='{ExpectedTexts.LOGOUT_BUTTON_TEXT}']"))
        ).click()
        

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//button[text()='{ExpectedTexts.LOGIN_BUTTON_TEXT}']"))
        ).is_displayed()