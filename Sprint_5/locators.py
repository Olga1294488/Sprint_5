from selenium.webdriver.common.by import By
class MainPageLocators:
    # Главная страница
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт" на главной
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка "Личный кабинет" в шапке
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка "Конструктор" в шапке
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")  # Логотип Stellar Burgers
    
 # Разделы конструктора
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::div") 
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::div")
    
    # Активный раздел
    ACTIVE_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
    
    # Кнопка оформления заказа (появляется после входа)
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")


class LoginPageLocators:
    # Страница входа
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # <- ЭТОТ ЛОКАТОР ДОЛЖЕН БЫТЬ!
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")


class RegistrationPageLocators:
    # Страница регистрации
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Поле ввода имени
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле ввода Email
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")  # Поле ввода пароля
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # Ссылка на вход


class ProfilePageLocators:
    # Страница профиля
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")  # Ссылка "Профиль" в ЛК
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")  # Ссылка "История заказов"
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка "Выход"
    
    # Альтернативные локаторы на случай изменения верстки
    PROFILE_LINK_ALT = (By.XPATH, "//a[contains(text(), 'Профиль')]")
    LOGOUT_BUTTON_ALT = (By.XPATH, "//button[contains(text(), 'Выход')]")


class ForgotPasswordPageLocators:
    # Страница восстановления пароля
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # Ссылка на вход


class ErrorMessages:
    # Сообщения об ошибках
    INCORRECT_PASSWORD = (By.XPATH, "//p[text()='Некорректный пароль']")  # Ошибка некорректного пароля