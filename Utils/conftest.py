import datetime
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from TestData.Testdata import FormyData

def capture_screenshot(driver,test_name):
    folder = "Screenshots/"+test_name+"/"
    os.makedirs(folder,exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"{test_name}+{timestamp}+.png"
    file_path = os.path.join(folder, filename)

    driver.save_screenshot(file_path)
    return file_path

@pytest.fixture(scope="session")
def setup_browser():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.implicitly_wait(25)
    driver.get(FormyData.url)

    yield driver

    driver.quit()