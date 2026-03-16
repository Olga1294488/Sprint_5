from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import generate_unique_email, generate_random_string
import json
import time


def create_test_user():
    """Создание тестового пользователя"""
    
    print("🚀 СОЗДАНИЕ ТЕСТОВОГО ПОЛЬЗОВАТЕЛЯ")
    print("=" * 60)
    
    # Генерируем данные
    user_email = generate_unique_email()
    user_password = generate_random_string(8)
    user_name = "Test User"
    
    print(f"📧 Email: {user_email}")
    print(f"🔑 Пароль: {user_password}")
    print(f"👤 Имя: {user_name}")
    
    # Запускаем браузер
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    try:
        # Открываем сайт
        print("\n1. Открываем сайт...")
        driver.get("https://stellarburgers.education-services.ru/")
        time.sleep(2)
        
        # Переходим на страницу входа
        print("2. Переходим на страницу входа...")
        login_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))
        )
        login_btn.click()
        time.sleep(1)
        
        # Переходим на регистрацию
        print("3. Переходим на страницу регистрации...")
        register_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Зарегистрироваться']"))
        )
        register_link.click()
        time.sleep(1)
        
        # Заполняем форму
        print("4. Заполняем форму регистрации...")
        
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='Имя']/following-sibling::input"))
        )
        name_input.send_keys(user_name)
        
        email_input = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")
        email_input.send_keys(user_email)
        
        password_input = driver.find_element(By.XPATH, "//input[@type='password']")
        password_input.send_keys(user_password)
        
        # Нажимаем кнопку регистрации
        print("5. Отправляем форму...")
        register_btn = driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']")
        register_btn.click()
        time.sleep(2)
        
        # Проверяем, что появилась форма входа
        print("6. Проверяем результат...")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Войти']"))
        )
        print("✅ Регистрация успешна!")
        
        # Сохраняем данные
        user_data = {
            "email": user_email,
            "password": user_password,
            "name": user_name
        }
        
        with open("test_user.json", "w") as f:
            json.dump(user_data, f, indent=2)
        
        print("\n📁 Данные сохранены в test_user.json")
        
        # Пробуем войти
        print("\n🔑 Пробуем войти с новым пользователем...")
        
        email_input = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")
        email_input.send_keys(user_email)
        
        password_input = driver.find_element(By.XPATH, "//input[@type='password']")
        password_input.send_keys(user_password)
        
        login_btn = driver.find_element(By.XPATH, "//button[text()='Войти']")
        login_btn.click()
        time.sleep(2)
        
        # Проверяем вход
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//button[text()='Оформить заказ']"))
            )
            print("✅ Вход выполнен успешно!")
        except:
            print("❌ Вход не выполнен")
        
        print("\n" + "=" * 60)
        print("🎉 Готово! Теперь можно запускать тесты.")
        
    finally:
        time.sleep(3)
        driver.quit()


if __name__ == "__main__":
    create_test_user()