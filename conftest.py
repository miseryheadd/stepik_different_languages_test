import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="Choose language, please")


@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")
    if browser_language is None:
        raise pytest.UsageError("Please select language with --language option.")
    else:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
        options.add_experimental_option('excludeSwitches', ['enable-logging'])  # fixes "devtools listening..." message
        print("\nstarting browser...")
        browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquiting browser..")
    browser.quit()
