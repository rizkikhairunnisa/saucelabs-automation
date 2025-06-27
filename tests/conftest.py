import sys
import os
import pytest
from selenium import webdriver

# Tambahkan path root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()
