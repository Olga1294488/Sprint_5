import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    """Добавление кастомных опций командной строки"""
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help='Выберите браузер: chrome или firefox'
    )


@pytest.fixture
def driver(request):
    """Фикстура для инициализации драйвера браузера"""
    browser = request.config.getoption('--browser')
    
    if browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        print("\n🔵 Запущен Chrome браузер")
    elif browser == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        print("\n🟠 Запущен Firefox браузер")
    else:
        raise ValueError(f"Неподдерживаемый браузер: {browser}")
    
    driver.maximize_window()
    driver.implicitly_wait(10)
    
    yield driver
    
    print(f"\n🛑 Закрываем браузер {browser}")
    driver.quit()
