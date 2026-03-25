import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators, LoginPageLocators, ProfilePageLocators
from urls import Urls
from data import UserData

class TestProfile:
    def login(self, driver):
        driver.get(Urls.BASE_URL)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON)
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(UserData.EXISTING_USER_EMAIL)
        
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(UserData.EXISTING_USER_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        ).is_displayed()
    
    def test_go_to_personal_account(self, driver):
        self.login(driver)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_LINK)
        ).is_displayed()
        assert "profile" in driver.current_url or "account" in driver.current_url
    
    def test_go_to_constructor_from_profile(self, driver):
        self.login(driver)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_LINK)
        )
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
        ).click()
        
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        ).is_displayed()
    
    def test_go_to_main_from_profile_by_logo(self, driver):
        self.login(driver)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_LINK)
        )
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGO)
        ).click()
        
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        ).is_displayed()
    
    def test_logout(self, driver):
        self.login(driver)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_LINK)
        )
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)
        ).click()
        
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        ).is_displayed()