import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setup_teardown():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_google_search_selenium_python(setup_teardown):
    driver = setup_teardown
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("selenium python")
    search_box.submit()
    driver.implicitly_wait(10)
    while driver.title == "Google":
        pass
    print("page title", driver.title)
    assert "selenium" in driver.title.lower(), "test failed: title mismatch"