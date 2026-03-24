import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators, LoginPageLocators, ErrorMessages
from data import Urls, UserGenerator


class TestRegisterAndSave:
    @pytest.fixture
    def new_user_data(self):
        return {
            "email": UserGenerator.generate_email(),
            "password": UserGenerator.generate_password(8),
            "name": UserGenerator.generate_name()
        }
    
    def test_successful_registration_shows_login_page(self, driver, user_helper, new_user_data):
        email = new_user_data["email"]
        password = new_user_data["password"]
        name = new_user_data["name"]
        
        user_helper.register_new_user(email, password, name)
        
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        ).is_displayed()
    
    def test_registered_user_can_login(self, driver, user_helper, new_user_data):
        email = new_user_data["email"]
        password = new_user_data["password"]
        name = new_user_data["name"]
        
        user_helper.register_new_user(email, password, name)
        
        driver.get(Urls.BASE_URL)
        user_helper.login_user(email, password)
        
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        ).is_displayed()
    
    def test_registration_with_existing_email_shows_error(self, driver, user_helper, new_user_data):
        email = new_user_data["email"]
        password = new_user_data["password"]
        name = new_user_data["name"]
        
        user_helper.register_new_user(email, password, name)
        
        driver.get(Urls.BASE_URL)
        user_helper.go_to_registration_page()
        user_helper.fill_registration_form(name, email, password)
        
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ErrorMessages.USER_ALREADY_EXISTS)
        ).is_displayed()