from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import UserGenerator, Urls
import json


class UserHelper:
    """Хелпер для работы с пользователями"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def register_new_user(self, email=None, password=None, name=None):
        """Регистрация нового пользователя"""
        
        # Генерируем данные если не переданы
        email = email or UserGenerator.generate_email()
        password = password or UserGenerator.generate_password(8)
        name = name or UserGenerator.generate_name()
        
        # Открываем сайт
        self.driver.get(Urls.BASE_URL)
        
        # Переходим на страницу регистрации
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))
        ).click()
        
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Зарегистрироваться']"))
        ).click()
        
        # Заполняем форму
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='Имя']/following-sibling::input"))
        ).send_keys(name)
        
        self.driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(email)
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
        
        # Ждем появления формы входа
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Войти']"))
        )
        
        return {"email": email, "password": password, "name": name}
    
    def login_user(self, email, password):
        """Вход пользователя"""
        self.driver.get(Urls.BASE_URL)
        
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))
        ).click()
        
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='Email']/following-sibling::input"))
        ).send_keys(email)
        
        self.driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        
        # Ждем успешного входа
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Оформить заказ']"))
        )
    
    def save_user_to_file(self, user_data, filename="user_data.json"):
        """Сохранение данных пользователя в файл"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(user_data, f, indent=2)
        print(f"📁 Данные сохранены в {filename}")