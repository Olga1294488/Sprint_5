import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators
from data import Urls, ExpectedTexts


class TestConstructor:
    """Тесты для конструктора бургеров"""
    
    def test_go_to_buns_section(self, driver):
        """Переход к разделу 'Булки'"""
        driver.get(Urls.BASE_URL)
        
        # Ждем загрузки страницы
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.BUNS_SECTION)
        )
        
        # Кликаем на раздел "Соусы"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.SAUCES_SECTION)
        ).click()
        
        # Ждем, что раздел "Соусы" стал активным
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(MainPageLocators.ACTIVE_SECTION, ExpectedTexts.SAUCES_SECTION)
        )
        
        # Кликаем на раздел "Булки"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.BUNS_SECTION)
        ).click()
        
        # Проверяем, что раздел "Булки" стал активным
        assert WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(MainPageLocators.ACTIVE_SECTION, ExpectedTexts.BUNS_SECTION)
        )
    
    def test_go_to_sauces_section(self, driver):
        """Переход к разделу 'Соусы'"""
        driver.get(Urls.BASE_URL)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.SAUCES_SECTION)
        ).click()
        
        assert WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(MainPageLocators.ACTIVE_SECTION, ExpectedTexts.SAUCES_SECTION)
        )
    
    def test_go_to_fillings_section(self, driver):
        """Переход к разделу 'Начинки'"""
        driver.get(Urls.BASE_URL)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.FILLINGS_SECTION)
        ).click()
        
        assert WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(MainPageLocators.ACTIVE_SECTION, ExpectedTexts.FILLINGS_SECTION)
        )