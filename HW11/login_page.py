from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    USER_EMAIL = 'admin@yourstore.com'
    USER_PASS = 'admin'

    def __init__(self, driver: webdriver):
        self.driver = driver

    def get_email_input(self):
        wait = WebDriverWait(self.driver, 5)
        email = wait.until(EC.presence_of_element_located((By.ID, "Email")))
        return email

    def get_password_input(self):
        return self.driver.find_element(By.ID, "Password")

    def get_login_button(self):
        # button_login = driver.find_element(By.CLASS_NAME, "login-button")
        return self.driver.find_element(By.XPATH, "//button[text()='Log in']")

    def fill_credentials(self):
        email = self.get_email_input()
        email.clear()
        email.send_keys(self.USER_EMAIL)

        password = self.get_password_input()
        password.clear()
        password.send_keys(self.USER_PASS)

    def do_login(self):
        self.fill_credentials()
        self.get_login_button().click()