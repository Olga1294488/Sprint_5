import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from data import TestData
import time


class TestProfileVisualDebug:
    """Визуальная отладка тестов профиля"""
    
    def test_manual_step_by_step(self, driver):
        """Пошаговое выполнение с паузами"""
        
        print("\n🔍 ПОШАГОВАЯ ДИАГНОСТИКА")
        print("=" * 60)
        
        # Шаг 1: Открываем сайт
        print("\n1. Открываем сайт...")
        driver.get(TestData.BASE_URL)
        time.sleep(3)
        print(f"   URL: {driver.current_url}")
        driver.save_screenshot("step1_main_page.png")
        
        # Шаг 2: Ищем кнопку входа
        print("\n2. Ищем кнопку 'Войти в аккаунт'...")
        try:
            login_btn = driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']")
            print(f"   ✅ Найдена: {login_btn.text}")
            login_btn.click()
            time.sleep(2)
            driver.save_screenshot("step2_login_page.png")
        except:
            print("   ❌ Кнопка не найдена!")
            # Пробуем другие варианты
            buttons = driver.find_elements(By.TAG_NAME, "button")
            print(f"   Все кнопки на странице:")
            for i, btn in enumerate(buttons):
                if btn.text:
                    print(f"     {i}: '{btn.text}'")
            return
        
        # Шаг 3: Заполняем форму входа
        print("\n3. Заполняем форму входа...")
        try:
            # Поле email
            email_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='text']"))
            )
            email_input.send_keys(TestData.EXISTING_USER_EMAIL)
            print(f"   ✅ Email введен: {TestData.EXISTING_USER_EMAIL}")
            
            # Поле пароля
            password_input = driver.find_element(By.XPATH, "//input[@type='password']")
            password_input.send_keys(TestData.EXISTING_USER_PASSWORD)
            print("   ✅ Пароль введен")
            
            # Кнопка входа
            submit_btn = driver.find_element(By.XPATH, "//button[text()='Войти']")
            submit_btn.click()
            print("   ✅ Кнопка входа нажата")
            time.sleep(3)
            driver.save_screenshot("step3_after_login.png")
        except Exception as e:
            print(f"   ❌ Ошибка: {e}")
            return
        
        # Шаг 4: Проверяем успешность входа
        print("\n4. Проверяем успешность входа...")
        try:
            order_btn = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[text()='Оформить заказ']"))
            )
            print(f"   ✅ Вход выполнен, найдена кнопка: {order_btn.text}")
        except:
            print("   ❌ Кнопка 'Оформить заказ' не найдена")
            print(f"   Текущий URL: {driver.current_url}")
            # Сохраняем HTML для анализа
            with open("after_login.html", "w", encoding="utf-8") as f:
                f.write(driver.page_source)
            print("   📄 HTML сохранен в after_login.html")
            return
        
        # Шаг 5: Переходим в профиль
        print("\n5. Переходим в профиль...")
        try:
            profile_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))
            )
            print(f"   ✅ Найдена ссылка на профиль")
            profile_link.click()
            time.sleep(3)
            driver.save_screenshot("step5_profile_page.png")
            print(f"   URL после перехода: {driver.current_url}")
        except Exception as e:
            print(f"   ❌ Ошибка: {e}")
            # Пробуем найти все элементы с текстом
            elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'Личный')]")
            if elements:
                print(f"   Найдены элементы с 'Личный':")
                for el in elements:
                    print(f"     Тег: {el.tag_name}, Текст: '{el.text}'")
            return
        
        # Шаг 6: Анализируем страницу профиля
        print("\n6. Анализируем страницу профиля...")
        
        # Сохраняем HTML
        with open("profile_page.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        print("   📄 HTML профиля сохранен в profile_page.html")
        
        # Ищем все ссылки
        links = driver.find_elements(By.TAG_NAME, "a")
        print(f"\n   Найдено ссылок: {len(links)}")
        profile_links = []
        for i, link in enumerate(links):
            if link.text:
                print(f"     [{i}] Текст: '{link.text}'")
                if "профиль" in link.text.lower():
                    profile_links.append(link)
        
        # Ищем все кнопки
        buttons = driver.find_elements(By.TAG_NAME, "button")
        print(f"\n   Найдено кнопок: {len(buttons)}")
        logout_buttons = []
        for i, btn in enumerate(buttons):
            if btn.text:
                print(f"     [{i}] Текст: '{btn.text}'")
                if "выход" in btn.text.lower():
                    logout_buttons.append(btn)
        
        # Результаты
        print("\n📊 РЕЗУЛЬТАТЫ ПОИСКА:")
        if profile_links:
            print(f"   ✅ Найдено ссылок с 'профиль': {len(profile_links)}")
            for link in profile_links:
                print(f"      - '{link.text}' (тег: {link.tag_name})")
        else:
            print("   ❌ Ссылки 'Профиль' не найдены")
        
        if logout_buttons:
            print(f"   ✅ Найдено кнопок с 'выход': {len(logout_buttons)}")
            for btn in logout_buttons:
                print(f"      - '{btn.text}' (тег: {btn.tag_name})")
        else:
            print("   ❌ Кнопки 'Выход' не найдены")
        
        print("\n" + "=" * 60)