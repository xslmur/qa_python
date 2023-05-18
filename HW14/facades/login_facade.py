import allure
from facades.facade_base import FacadeBase


class LoginFacade(FacadeBase):
    def __init__(self):
        super().__init__()

    @allure.step("Fill email and password fields")
    def fill_credentials(self, email, password):
        self._login_page.fill_credentials(email, password)

    @allure.step("Click Sign-in button")
    def click_signin_button(self):
        self._login_page.get_sign_in_button().click()

    @allure.step("Click Login button")
    def click_login_button(self):
        self._login_page.get_login_button().click()

    @allure.step("do WEB UI login")
    def do_login(self, email, password):
        self.click_signin_button()
        self.fill_credentials(email, password)
        self.click_login_button()

    def check_if_profile_displayed(self):
        return self._garage_page.get_my_profile_button().is_displayed()
