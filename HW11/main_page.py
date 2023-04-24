from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def get_logout_button(self):
        wait = WebDriverWait(self.driver, 5)
        logout_button = wait.until(
            EC.presence_of_element_located((
                By.XPATH, "//a[@class='nav-link' and @href='/logout']")))
        return logout_button
