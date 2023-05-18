import allure
from facades.facade_base import FacadeBase


class GarageFacade(FacadeBase):
    def __init__(self):
        super().__init__()

    @allure.step("search for Profile button")
    def get_my_profile_button(self):
        return self._garage_page.get_my_profile_button()

    @allure.step("click Profile button")
    def click_my_profile_button(self):
        self.get_my_profile_button().click()

    @allure.step("click addCar button")
    def click_add_car_button(self):
        self._garage_page.get_add_car_button().click()

    @allure.step("click modifyCar button")
    def click_modify_car_button(self):
        self._garage_page.get_modify_car_button().click()

    @allure.step("click Add button on the car add form")
    def click_form_add_car_button(self):
        self._garage_page.get_form_add_car_button().click()

    @allure.step("click Save button on the car modify form")
    def click_form_save_car_button(self):
        self._garage_page.get_form_save_car_button().click()

    @allure.step("click car Remove button on the car modify form")
    def click_form_remove_car_button(self):
        self._garage_page.get_form_remove_car_button().click()

    @allure.step("click Remove confirm button on the car remove confirmation form")
    def click_form_remove_car_confirm_button(self):
        self._garage_page.get_form_remove_car_confirm_button().click()

    @allure.step('select car Brand')
    def select_car_brand(self, text):
        self._garage_page.get_form_brand_field().select_by_visible_text(text)

    @allure.step('select car Model')
    def select_car_model(self, text):
        self._garage_page.get_form_model_field().select_by_visible_text(text)

    @allure.step('fill car mileage')
    def fill_car_mileage(self, mileage):
        self._garage_page.get_form_mileage_field().fill_field(mileage)
