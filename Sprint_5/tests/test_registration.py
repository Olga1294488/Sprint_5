from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators, RegistrationPageLocators, LoginPageLocators, ErrorMessages
from data import TestData, generate_unique_email


class TestRegistration:
    
    def test_successful_registration(self, driver):
        """Тест успешной регистрации"""
        driver.get(TestData.BASE_URL)
        
        # Клик по кнопке "Войти в аккаунт"
        driver.find_element(*MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
        
        # Клик по ссылке "Зарегистрироваться"
        driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
        
        # Заполнение формы регистрации
        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("Иван Иванов")
        
        unique_email = generate_unique_email()
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(unique_email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(TestData.VALID_PASSWORD)
        
        # Клик по кнопке "Зарегистрироваться"
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        
        # Ожидание появления формы входа
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )
        
        # Проверка, что появилась страница входа
        assert driver.find_element(*LoginPageLocators.LOGIN_BUTTON).is_displayed()
    
    def test_registration_invalid_password(self, driver):
        """Тест регистрации с некорректным паролем"""
        driver.get(TestData.BASE_URL)
        
        # Переход на страницу регистрации
        driver.find_element(*MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
        
        # Заполнение формы с невалидным паролем
        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("Иван Иванов")
        
        unique_email = generate_unique_email()
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(unique_email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(TestData.INVALID_PASSWORD)
        
        # Клик по кнопке "Зарегистрироваться"
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        
        # Проверка появления ошибки
        error_message = driver.find_element(*ErrorMessages.INCORRECT_PASSWORD)
        assert error_message.is_displayed()
