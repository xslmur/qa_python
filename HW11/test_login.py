from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from login_page import LoginPage
from main_page import MainPage
from driver import Driver


class TestLogin:
    def setup_class(self):
        self.driver = Driver.get_chrome_driver()

    def setup_method(self):
        self.driver.get("https://admin-demo.nopcommerce.com/login")
        self.login_page = LoginPage()
        self.main_page = MainPage()

    def test_login(self):
        # wait for the login form and do login
        self.login_page.do_login()

        # check we have logout link on the main page and click it
        logout = self.main_page.get_logout_button()
        assert logout
        logout.click()

        # wait for login form to ensure we had successful logout
        email = self.login_page.get_email_input()
        assert email

    def teardown_method(self):
        pass

    def teardown_class(self):
        self.driver.close()
