import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators
from urls import Urls
from data import ExpectedTexts


class TestConstructor:
    """Тесты для конструктора бургеров"""
    
    @pytest.mark.parametrize("section_locator, section_name", [
        (MainPageLocators.SAUCES_SECTION, ExpectedTexts.SAUCES_SECTION),
        (MainPageLocators.FILLINGS_SECTION, ExpectedTexts.FILLINGS_SECTION),
        (MainPageLocators.BUNS_SECTION, ExpectedTexts.BUNS_SECTION)
    ])
    def test_go_to_section(self, driver, section_locator, section_name):
        """Параметризованный тест: переход к разделам конструктора"""
        driver.get(Urls.BASE_URL)
        
        # Ждем загрузки страницы
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(section_locator)
        )
        
        # Для раздела "Булки" нужно сначала кликнуть на другой раздел
        if section_name == ExpectedTexts.BUNS_SECTION:
            # Сначала кликаем на "Соусы", чтобы уйти с активного раздела
            sauces_section = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(MainPageLocators.SAUCES_SECTION)
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", sauces_section)
            sauces_section.click()
            
            # Ждем, что "Соусы" стали активными
            WebDriverWait(driver, 10).until(
                EC.text_to_be_present_in_element(MainPageLocators.ACTIVE_SECTION, ExpectedTexts.SAUCES_SECTION)
            )
        
        # Скроллим до нужного элемента
        element = driver.find_element(*section_locator)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        
        # Кликаем на раздел
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(section_locator)
        ).click()
        
        # Проверяем, что раздел стал активным
        assert WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(MainPageLocators.ACTIVE_SECTION, section_name)
        )