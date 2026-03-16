import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators
from data import TestData


class TestConstructor:
    """Тесты для конструктора бургеров"""
    
    def test_go_to_buns_section(self, driver):
        """Переход к разделу 'Булки'"""
        driver.get(TestData.BASE_URL)
        
        # Ждем загрузки страницы
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.BUNS_SECTION)
        )
        
        # Клик по разделу "Соусы" (чтобы уйти с булок)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.SAUCES_SECTION)
        ).click()
        
        # Небольшая пауза для анимации
        import time
        time.sleep(1)
        
        # Клик по разделу "Булки"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.BUNS_SECTION)
        ).click()
        
        # Проверка, что раздел "Булки" активен
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(MainPageLocators.ACTIVE_SECTION, "Булки")
        )
        active_section = driver.find_element(*MainPageLocators.ACTIVE_SECTION)
        assert "Булки" in active_section.text
        print("✅ Переход к разделу 'Булки' работает")
    
    def test_go_to_sauces_section(self, driver):
        """Переход к разделу 'Соусы'"""
        driver.get(TestData.BASE_URL)
        
        # Ждем загрузки страницы
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.SAUCES_SECTION)
        )
        
        # Клик по разделу "Соусы"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.SAUCES_SECTION)
        ).click()
        
        # Проверка, что раздел "Соусы" активен
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(MainPageLocators.ACTIVE_SECTION, "Соусы")
        )
        active_section = driver.find_element(*MainPageLocators.ACTIVE_SECTION)
        assert "Соусы" in active_section.text
        print("✅ Переход к разделу 'Соусы' работает")
    
    def test_go_to_fillings_section(self, driver):
        """Переход к разделу 'Начинки'"""
        driver.get(TestData.BASE_URL)
        
        # Ждем загрузки страницы
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.FILLINGS_SECTION)
        )
        
        # Клик по разделу "Начинки"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.FILLINGS_SECTION)
        ).click()
        
        # Проверка, что раздел "Начинки" активен
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(MainPageLocators.ACTIVE_SECTION, "Начинки")
        )
        active_section = driver.find_element(*MainPageLocators.ACTIVE_SECTION)
        assert "Начинки" in active_section.text
        print("✅ Переход к разделу 'Начинки' работает")