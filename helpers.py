from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators
from data import Urls
import json


class UserHelper:
    """Хелпер для работы с пользователями"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    # методы для навигации   
    def go_to_main_page(self):
        """Переход на главную страницу"""
        self.driver.get(Urls.BASE_URL)
    
    def go_to_login_page(self):
        """Переход на страницу входа"""
        self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON)
        ).click()
    
    def go_to_registration_page(self):
        """Переход на страницу регистрации"""
        self.go_to_login_page()
        self.wait.until(
            EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)
        ).click()
    
    # методы для заполнения форм
    def fill_registration_form(self, name, email, password):
        """Заполнение формы регистрации"""
        self.wait.until(
            EC.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT)
        ).send_keys(name)
        
        self.driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
    
    def fill_login_form(self, email, password):
        """Заполнение формы входа"""
        self.wait.until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(email)
        
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    
    #  методы для ожидания   
    def wait_for_login_page(self):
        """Ожидание появления страницы входа"""
        self.wait.until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )
    
    def wait_for_main_page(self):
        """Ожидание появления главной страницы после входа"""
        self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
    
    #  комплексные методы (собирают атомарные)
    def register_new_user(self, email, password, name):
        """
        Регистрация нового пользователя
        Возвращает словарь с данными пользователя
        """
        self.go_to_main_page()
        self.go_to_registration_page()
        self.fill_registration_form(name, email, password)
        self.wait_for_login_page()
        
        return {
            "email": email,
            "password": password,
            "name": name
        }
    
    def login_user(self, email, password):
        """Вход существующего пользователя"""
        self.go_to_main_page()
        self.go_to_login_page()
        self.fill_login_form(email, password)
        self.wait_for_main_page()
    
    # вспомогательные методы 
    def save_user_to_file(self, user_data, filename="user_data.json"):
        """Сохранение данных пользователя в файл"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(user_data, f, indent=2)