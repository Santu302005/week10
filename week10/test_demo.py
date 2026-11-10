import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
@pytest.fixture
def setup_teardown():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver  
    driver.quit()
def test_google_search(setup_teardown):
    driver = setup_teardown
    driver.get("https://www.google.com")
    print("page title", driver.title)
    assert "Google" in driver.title, "test failed: title mismatch"
    print("test completed successfully")