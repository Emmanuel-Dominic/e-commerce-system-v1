import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# @pytest.fixture(scope="module")
@pytest.fixture(scope="function")
def chrome_browser_instance(request):
    service=Service(ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--no-sandbox')
    # chrome_options.headless = False
    chrome_options.add_argument('--headless')
    # browser = webdriver.Chrome(chrome_options=options) # Deprecated to webdriver.ChromeOptions() or ...
    browser = webdriver.Chrome(service=service, options=chrome_options)
    yield browser
    browser.close()
