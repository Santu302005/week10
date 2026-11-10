from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
def test_google_title():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com")
    print("Page Title:",driver.title)
    assert "Google" in driver.title, "Test Failed: Title mismatch"
   

    print("Test Completed Successfully")
    driver.quit()
if __name__ == "__main__":
    test_google_title()