import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


# добавляем параметр запуска тестов в командной строке(чем запускать, хромом или фаерфоксом + язык) По умолчанию хром
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None, help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None, help="Choose your language")


# Запуск браузера(для каждой функции)
@pytest.fixture(scope="function")  # по умолчанию запускается для каждой функции
def browser(request):
    browser_name = request.config.getoption("browser_name")  # получаем параметр командной строки browser_name
    language = request.config.getoption("language")  # получаем параметр командной строки language
    browser = None
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        print("\nstart Сhrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart Firefox browser for test..")
        firefox_options = FirefoxOptions()
        firefox_options.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=firefox_options)  # автоматически устанавливаем последнюю версию браузера
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    time.sleep(10)
    print("\nquit browser..")
    browser.quit()

