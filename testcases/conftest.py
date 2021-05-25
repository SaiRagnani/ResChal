import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup():
    global driver
    driver= webdriver.Chrome(executable_path="C:\\Users\\Nani\\Desktop\\WebDrivers\\chromedriver.exe")
    driver.get("file:///C:/Users/Nani/Desktop/index.html")
    driver.implicitly_wait(5)
    driver.maximize_window()
    return driver
