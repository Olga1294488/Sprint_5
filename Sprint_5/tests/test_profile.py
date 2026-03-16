import pytest
from selenium.webdriver.common.by import By  # ВАЖНО: добавляем этот импорт!
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators, LoginPageLocators, ProfilePageLocators
from data import TestData
import time


class TestProfile:
    """Тесты для личного кабинета"""
    
    def login_user(self, driver):
        """Вспомогательный метод для входа пользователя"""
        driver.get(TestData.BASE_URL)
        
        # Ждем и кликаем по кнопке "Войти в аккаунт"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON)
        ).click()
        
        # Ждем поле email и заполняем
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(TestData.EXISTING_USER_EMAIL)
        
        # Заполняем пароль
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TestData.EXISTING_USER_PASSWORD)
        
        # Кликаем кнопку входа
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Ждем успешного входа (появление кнопки "Оформить заказ")
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        print("✅ Вход выполнен успешно")
    
    def test_go_to_personal_account(self, driver):
        """Переход в личный кабинет"""
        # Входим в систему
        self.login_user(driver)
        
        # Даем время для полной загрузки страницы
        time.sleep(1)
        
        # Клик по кнопке "Личный кабинет"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        # Проверка перехода в личный кабинет
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_LINK)
        )
        assert driver.find_element(*ProfilePageLocators.PROFILE_LINK).is_displayed()
        print("✅ Переход в личный кабинет выполнен")
    
    def test_go_to_constructor_from_profile(self, driver):
        """Переход из личного кабинета в конструктор по клику на 'Конструктор'"""
        # Входим в систему
        self.login_user(driver)
        
        # Даем время для полной загрузки страницы
        time.sleep(1)
        
        # Переходим в профиль
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        # Ждем загрузки профиля
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_LINK)
        )
        
        # Клик по кнопке "Конструктор"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
        ).click()
        
        # Проверка перехода на главную
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed()
        print("✅ Переход в конструктор выполнен")
    
    def test_go_to_main_from_profile_by_logo(self, driver):
        """Переход из личного кабинета на главную по клику на логотип"""
        # Входим в систему
        self.login_user(driver)
        
        # Даем время для полной загрузки страницы
        time.sleep(1)
        
        # Переходим в профиль
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        # Ждем загрузки профиля
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_LINK)
        )
        
        # Клик по логотипу
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGO)
        ).click()
        
        # Проверка перехода на главную
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed()
        print("✅ Переход по логотипу выполнен")
    
    def test_logout(self, driver):
        """Выход из аккаунта"""
        # Входим в систему
        self.login_user(driver)
        
        # Даем время для полной загрузки страницы
        time.sleep(1)
        
        # Переходим в профиль
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        # Ждем загрузки профиля
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_LINK)
        )
        
        # Пробуем найти и кликнуть кнопку выхода (с запасным вариантом)
        try:
            logout_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)
            )
        except:
            # Если не нашли по основному локатору, пробуем альтернативный
            logout_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON_ALT)
            )
        
        # Скроллим до элемента, чтобы убедиться, что он видим
        driver.execute_script("arguments[0].scrollIntoView(true);", logout_button)
        time.sleep(1)
        
        # Кликаем
        logout_button.click()
        
        # Проверка выхода (появление кнопки "Войти")
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )
        assert driver.find_element(*LoginPageLocators.LOGIN_BUTTON).is_displayed()
        print("✅ Выход из аккаунта выполнен")