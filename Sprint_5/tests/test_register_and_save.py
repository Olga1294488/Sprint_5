import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from data import generate_unique_email, generate_random_string, TestData
import json


class TestRegisterAndSave:
    """Регистрация нового пользователя и сохранение данных"""
    
    def test_register_new_user(self, driver):
        """Регистрация нового пользователя и сохранение данных в файл"""
        
        print("\n🔐 РЕГИСТРАЦИЯ НОВОГО ПОЛЬЗОВАТЕЛЯ")
        print("=" * 60)
        
        # Генерируем уникальные данные
        user_email = generate_unique_email()
        user_password = generate_random_string(8)
        user_name = "Test User"
        
        print(f"📧 Email: {user_email}")
        print(f"🔑 Пароль: {user_password}")
        
        # Открываем сайт
        driver.get(TestData.BASE_URL)
        
        # Переходим на страницу регистрации
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Зарегистрироваться']"))
        ).click()
        
        # Заполняем форму
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='Имя']/following-sibling::input"))
        )
        name_input.send_keys(user_name)
        
        email_input = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")
        email_input.send_keys(user_email)
        
        password_input = driver.find_element(By.XPATH, "//input[@type='password']")
        password_input.send_keys(user_password)
        
        register_btn = driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']")
        register_btn.click()
        
        # Проверяем, что появилась страница входа
        login_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Войти']"))
        )
        
        # Вместо return используем assert для проверки
        assert login_btn is not None, "Кнопка 'Войти' не появилась после регистрации"
        assert login_btn.is_displayed(), "Кнопка 'Войти' не отображается на странице"
        
        # Сохраняем данные в файл
        user_data = {
            "email": user_email,
            "password": user_password,
            "name": user_name
        }
        
        with open("test_user.json", "w") as f:
            json.dump(user_data, f, indent=2)
        
        print("\n✅ Регистрация успешна!")
        print("📁 Данные сохранены в test_user.json")
        
        # Проверяем, что файл создался
        import os
        assert os.path.exists("test_user.json"), "Файл test_user.json не создан"
        
        print("=" * 60)