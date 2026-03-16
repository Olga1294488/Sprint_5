import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from data import TestData
import json


class TestLoginWithNewUser:
    """Тесты входа с новым пользователем"""
    
    def load_user_data(self):
        """Загрузка данных пользователя"""
        try:
            with open("test_user.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            pytest.skip("Нет файла с данными пользователя. Сначала запусти setup_test_user.py")
    
    def test_login_with_new_user(self, driver):
        """Тест входа с новым пользователем"""
        user_data = self.load_user_data()
        
        print(f"\n🔐 Вход с пользователем: {user_data['email']}")
        
        # Открываем сайт
        driver.get(TestData.BASE_URL)
        
        # Клик по кнопке входа
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))
        ).click()
        
        # Заполняем форму
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='Email']/following-sibling::input"))
        )
        email_input.send_keys(user_data["email"])
        
        password_input = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")
        password_input.send_keys(user_data["password"])
        
        login_btn = driver.find_element(By.XPATH, "//button[text()='Войти']")
        login_btn.click()
        
        # Проверяем вход
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Оформить заказ']"))
        )
        
        print("✅ Вход выполнен успешно!")