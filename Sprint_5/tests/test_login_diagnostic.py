import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from data import TestData
import time


class TestLoginDiagnostic:
    """Диагностика проблемы с входом"""
    
    def test_check_login_page_structure(self, driver):
        """Проверка структуры страницы входа"""
        
        print("\n🔍 ДИАГНОСТИКА СТРАНИЦЫ ВХОДА")
        print("=" * 60)
        
        # Шаг 1: Открываем главную
        print("\n1. Открываем главную страницу")
        driver.get(TestData.BASE_URL)
        time.sleep(2)
        driver.save_screenshot("01_main_page.png")
        print("   📸 Скриншот сохранен: 01_main_page.png")
        
        # Шаг 2: Ищем все кнопки на главной
        print("\n2. Анализируем кнопки на главной странице")
        buttons = driver.find_elements(By.TAG_NAME, "button")
        print(f"   Найдено кнопок: {len(buttons)}")
        for i, btn in enumerate(buttons):
            if btn.text:
                print(f"   [{i}] Текст: '{btn.text}'")
                print(f"       Class: {btn.get_attribute('class')}")
        
        # Шаг 3: Ищем кнопку входа
        print("\n3. Ищем кнопку 'Войти в аккаунт'")
        login_btn = None
        login_selectors = [
            "//button[text()='Войти в аккаунт']",
            "//button[contains(text(), 'Войти')]",
            "//a[text()='Войти']",
            "//a[contains(text(), 'Войти')]"
        ]
        
        for selector in login_selectors:
            try:
                elements = driver.find_elements(By.XPATH, selector)
                if elements:
                    print(f"   ✅ Найдено по: {selector}")
                    for el in elements:
                        print(f"      - Текст: '{el.text}', Тег: {el.tag_name}")
                        login_btn = el
                    break
            except:
                continue
        
        if not login_btn:
            print("   ❌ Кнопка входа не найдена!")
            print("   Сохраняю HTML для анализа...")
            with open("main_page.html", "w", encoding="utf-8") as f:
                f.write(driver.page_source)
            return
        
        # Шаг 4: Кликаем по кнопке входа
        print("\n4. Кликаем по кнопке входа")
        try:
            driver.execute_script("arguments[0].scrollIntoView(true);", login_btn)
            time.sleep(1)
            login_btn.click()
            time.sleep(2)
            driver.save_screenshot("02_login_page.png")
            print("   ✅ Клик выполнен")
        except Exception as e:
            print(f"   ❌ Ошибка клика: {e}")
            return
        
        # Шаг 5: Анализируем страницу входа
        print("\n5. Анализируем страницу входа")
        print(f"   Текущий URL: {driver.current_url}")
        
        # Поля ввода
        inputs = driver.find_elements(By.TAG_NAME, "input")
        print(f"\n   Найдено полей ввода: {len(inputs)}")
        for i, inp in enumerate(inputs):
            input_type = inp.get_attribute("type")
            input_name = inp.get_attribute("name")
            input_placeholder = inp.get_attribute("placeholder")
            print(f"   [{i}] type='{input_type}', name='{input_name}', placeholder='{input_placeholder}'")
        
        # Кнопки на странице входа
        buttons = driver.find_elements(By.TAG_NAME, "button")
        print(f"\n   Найдено кнопок: {len(buttons)}")
        for i, btn in enumerate(buttons):
            if btn.text:
                print(f"   [{i}] Текст: '{btn.text}'")
        
        # Ссылки
        links = driver.find_elements(By.TAG_NAME, "a")
        print(f"\n   Найдено ссылок: {len(links)}")
        for i, link in enumerate(links):
            if link.text:
                print(f"   [{i}] Текст: '{link.text}'")
        
        # Шаг 6: Пробуем заполнить форму
        print("\n6. Пробуем заполнить форму входа")
        try:
            # Ищем поле email
            email_field = None
            for inp in inputs:
                if inp.get_attribute("type") == "text" or "email" in inp.get_attribute("name", "").lower():
                    email_field = inp
                    break
            
            if email_field:
                email_field.send_keys(TestData.EXISTING_USER_EMAIL)
                print(f"   ✅ Email введен: {TestData.EXISTING_USER_EMAIL}")
            else:
                print("   ❌ Поле email не найдено")
            
            # Ищем поле пароля
            password_field = None
            for inp in inputs:
                if inp.get_attribute("type") == "password":
                    password_field = inp
                    break
            
            if password_field:
                password_field.send_keys(TestData.EXISTING_USER_PASSWORD)
                print("   ✅ Пароль введен")
            else:
                print("   ❌ Поле пароля не найдено")
            
            # Ищем кнопку отправки
            submit_btn = None
            for btn in buttons:
                if btn.text and "войти" in btn.text.lower():
                    submit_btn = btn
                    break
            
            if submit_btn:
                print(f"   ✅ Кнопка отправки найдена: '{submit_btn.text}'")
                submit_btn.click()
                time.sleep(2)
                driver.save_screenshot("03_after_login.png")
                print("   ✅ Клик по кнопке входа выполнен")
            else:
                print("   ❌ Кнопка отправки не найдена")
                
        except Exception as e:
            print(f"   ❌ Ошибка при заполнении формы: {e}")
        
        # Шаг 7: Проверяем результат
        print("\n7. Проверяем результат входа")
        print(f"   Текущий URL: {driver.current_url}")
        
        # Ищем кнопку "Оформить заказ"
        try:
            order_btn = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить')]"))
            )
            print(f"   ✅ Вход выполнен! Найдена кнопка: '{order_btn.text}'")
        except:
            print("   ❌ Вход не выполнен - кнопка 'Оформить заказ' не найдена")
            
        print("\n" + "=" * 60)