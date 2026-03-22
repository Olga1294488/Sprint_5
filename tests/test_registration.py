import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators, ErrorMessages
from data import Urls, RegistrationData, UserGenerator, ExpectedTexts


class TestRegistration:
    """Тесты регистрации"""
    
    def test_successful_registration(self, driver):
        """Успешная регистрация"""
        driver.get(Urls.BASE_URL)
        
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON)
        ).click()
        
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)
        ).click()
        
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT)
        ).send_keys(UserGenerator.generate_name())
        
        unique_email = UserGenerator.generate_email()
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(unique_email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(RegistrationData.get_valid_password())
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        
        assert WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        ).is_displayed()
    
    def test_registration_invalid_password(self, driver):
        """Регистрация с некорректным паролем"""
        driver.get(Urls.BASE_URL)
        
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON)
        ).click()
        
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)
        ).click()
        
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT)
        ).send_keys(UserGenerator.generate_name())
        
        unique_email = UserGenerator.generate_email()
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(unique_email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(RegistrationData.get_invalid_password())
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        
        error_message = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(ErrorMessages.INCORRECT_PASSWORD)
        )
        assert error_message.is_displayed()
        assert ExpectedTexts.INCORRECT_PASSWORD_ERROR in error_message.text