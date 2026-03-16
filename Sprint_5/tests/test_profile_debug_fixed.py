import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from data import TestData
import time


class TestProfileDebug:
    """Отладочные тесты для профиля"""
    
    def login_user(self, driver):
        """Вход в систему"""
        driver.get(TestData.BASE_URL)
        
        # Клик по кнопке "Войти в аккаунт"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))
        ).click()
        
        # Заполнение формы входа
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='text']"))
        )
        email_input.send_keys(TestData.EXISTING_USER_EMAIL)
        
        password_input = driver.find_element(By.XPATH, "//input[@type='password']")
        password_input.send_keys(TestData.EXISTING_USER_PASSWORD)
        
        submit_btn = driver.find_element(By.XPATH, "//button[text()='Войти']")
        submit_btn.click()
        
        # Ожидание успешного входа
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Оформить заказ']"))
        )
        print("✅ Вход выполнен")
    
    def test_find_profile_elements(self, driver):
        """Тест: поиск элементов на странице профиля"""
        self.login_user(driver)
        
        print("\n🔍 ПОИСК ЭЛЕМЕНТОВ ПРОФИЛЯ")
        print("=" * 50)
        
        # Переход в профиль
        profile_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))
        )
        profile_link.click()
        time.sleep(3)
        
        print(f"URL после перехода: {driver.current_url}")
        
        # Сохраняем скриншот
        driver.save_screenshot("profile_page.png")
        print("📸 Скриншот сохранен: profile_page.png")
        
        # Ищем все ссылки
        print("\n📌 ВСЕ ССЫЛКИ НА СТРАНИЦЕ:")
        links = driver.find_elements(By.TAG_NAME, "a")
        for i, link in enumerate(links):
            if link.text:
                print(f"  [{i}] Текст: '{link.text}'")
                print(f"      href: {link.get_attribute('href')}")
        
        # Ищем все кнопки
        print("\n📌 ВСЕ КНОПКИ НА СТРАНИЦЕ:")
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for i, btn in enumerate(buttons):
            if btn.text:
                print(f"  [{i}] Текст: '{btn.text}'")
        
        # Специальный поиск "Профиль"
        print("\n🔍 ПОИСК 'ПРОФИЛЬ':")
        profile_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'Профиль')]")
        for el in profile_elements:
            print(f"  ✅ Найдено: '{el.text}' (тег: {el.tag_name})")
        
        # Специальный поиск "Выход"
        print("\n🔍 ПОИСК 'ВЫХОД':")
        logout_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'Выход')]")
        for el in logout_elements:
            print(f"  ✅ Найдено: '{el.text}' (тег: {el.tag_name})")
    
    def test_try_different_selectors(self, driver):
        """Тест: пробуем разные селекторы для профиля"""
        self.login_user(driver)
        
        # Переход в профиль
        profile_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))
        )
        profile_link.click()
        time.sleep(2)
        
        print("\n🔍 ПРОБУЕМ РАЗНЫЕ СЕЛЕКТОРЫ")
        print("=" * 50)
        
        # Пробуем разные селекторы для элемента "Профиль"
        profile_selectors = [
            "//a[text()='Профиль']",
            "//a[contains(text(), 'Профиль')]",
            "//*[text()='Профиль']",
            "//*[contains(text(), 'Профиль')]",
            "//a[@href='/profile']",
            "//li/a[text()='Профиль']"
        ]
        
        print("\n📌 ПОИСК 'ПРОФИЛЬ':")
        for i, selector in enumerate(profile_selectors):
            try:
                element = driver.find_element(By.XPATH, selector)
                print(f"  [{i}] ✅ '{selector}' - НАЙДЕН: '{element.text}'")
            except:
                print(f"  [{i}] ❌ '{selector}' - НЕ НАЙДЕН")
        
        # Пробуем разные селекторы для кнопки "Выход"
        logout_selectors = [
            "//button[text()='Выход']",
            "//button[contains(text(), 'Выход')]",
            "//*[text()='Выход']",
            "//*[contains(text(), 'Выход')]",
            "//button[@class='Account_button__14Yp3']",
            "//a[text()='Выход']"
        ]
        
        print("\n📌 ПОИСК 'ВЫХОД':")
        for i, selector in enumerate(logout_selectors):
            try:
                element = driver.find_element(By.XPATH, selector)
                print(f"  [{i}] ✅ '{selector}' - НАЙДЕН: '{element.text}'")
            except:
                print(f"  [{i}] ❌ '{selector}' - НЕ НАЙДЕН")