import pytest
#from selenium import webdriver
from utils.constants import Url
#from selenium.webdriver.common.by import By
from playwright.sync_api import Page, expect
from tests.test_2 import p
import re
from playwright.sync_api import sync_playwright

"""
@pytest.fixture(scope="function")
def start_browser():
    #"Запуск браузера"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(r'C:/chromedriver/chromedriver.exe')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    yield driver

    #"Закрытие браузера"
    driver.quit()
"""


@pytest.fixture(scope="function")
def navigate_start_page():
    with sync_playwright() as play:
        browser = play.chromium.launch()
        page = browser.new_page()
        page.goto(Url.login_url)

        yield page

        browser.close()

    """
    def navigate_start_page(start_browser):
        driver = start_browser
        #"Переход на стартовую страницу")
        driver.get(Url.login_url)

        yield driver
    """


"""
@pytest.fixture(scope="function")
def fill_login_and_enter(navigate_start_page, username="standard_user", password="secret_sauce"):
    driver = navigate_start_page
    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    yield driver
"""
