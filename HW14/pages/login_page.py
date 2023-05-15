from selenium.webdriver.common.by import By
from .base_page_with_driver import BasePageWithDriver
from controls.button import Button
from controls.textbox import TextBox
from controls.label import Label
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePageWithDriver):
    def __init__(self):
        super().__init__()
        self._sign_in_button = None
        self._email_field = None
        self._password_field = None
        self._login_button = None
        self._email_incorrect_alert = None
        self._remember_me_button = None
        self._wrong_user_alert = None

    def get_sign_in_button(self):
        self._sign_in_button = Button(self._driver.find_element(By.XPATH, "//button[text()='Sign In']"))
        return self._sign_in_button

    def get_email_field(self):
        wait = WebDriverWait(self._driver, 5)
        self._email_field = TextBox(wait.until(EC.presence_of_element_located((By.ID, "signinEmail"))))
        return self._email_field

    def get_password_field(self):
        self._password_field = TextBox(self._driver.find_element(By.ID, "signinPassword"))
        return self._password_field

    def get_login_button(self):
        self._login_button = Button(self._driver.find_element(By.XPATH, "//button[text()='Login']"))
        return self._login_button

    def get_login_incorrect_alert(self):
        self._email_incorrect_alert = Label(self._driver.find_element(By.XPATH, "//p[text()='Email is incorrect']"))
        return self._email_incorrect_alert

    def get_remember_me_button(self):
        self._remember_me_button = Button(self._driver.find_element(By.ID, "remember"))
        return self._remember_me_button

    def get_wrong_user_alert(self):
        self._wrong_user_alert = Label(self._driver.find_element(By.XPATH, "//p[text()='Wrong email or password']"))
        return self._wrong_user_alert

    def fill_credentials(self, email, password):
        self.get_email_field().fill_field(email)
        self.get_password_field().fill_field(password)

    def do_login(self, email, password):
        self.get_sign_in_button().click()
        self.fill_credentials(email, password)
        self.get_login_button().click()
