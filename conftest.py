import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options



@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")
    driver = webdriver.Edge(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
