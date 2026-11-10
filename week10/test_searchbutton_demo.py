import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
@pytest.fixture
def setup_teardown():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver  
    driver.quit()
def test_google_search_button_exist(setup_teardown):
    driver = setup_teardown
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME,"q")
    search_box.send_keys(Keys.TAB)
    search_button = driver.find_elements(By.NAME, "btnK")
    assert any(button.is_displayed() for button in search_button), "google search button not visible"
    print("google search button is present and visible")