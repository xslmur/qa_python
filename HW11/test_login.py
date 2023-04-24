from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from login_page import LoginPage
from main_page import MainPage


class TestLogin:
    def setup_class(self):
        opts = Options()
        opts.add_argument("start-maximized")
        opts.add_argument('--user-data-dir=/home/sl/.config/chromium')
        self.driver = webdriver.Chrome(options=opts)

    def test_login(self):
        self.driver.get("https://admin-demo.nopcommerce.com/login")
        login_page = LoginPage(self.driver)
        login_page.do_login()

        main_page = MainPage(self.driver)
        logout = main_page.get_logout_button()
        assert logout
        logout.click()

    def teardown_class(self):
        self.driver.close()
