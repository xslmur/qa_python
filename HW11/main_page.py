from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base_page import BasePage


class MainPage(BasePage):
    def __init__(self):
        super().__init__()

    def get_logout_button(self):
        wait = WebDriverWait(self._driver, 5)
        logout_link = wait.until(
            EC.presence_of_element_located((
                By.XPATH, "//a[@class='nav-link' and @href='/logout']")))
        return logout_link
