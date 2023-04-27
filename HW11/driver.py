from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


class Driver:
    driver = None

    @staticmethod
    def get_chrome_driver() -> WebDriver:
        if Driver.driver is None:
            opts = Options()
            opts.add_argument("start-maximized")
            opts.add_argument('--user-data-dir=/home/sl/.config/chromium')
            Driver.driver = webdriver.Chrome(options=opts)
        return Driver.driver
