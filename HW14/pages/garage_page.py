from selenium.webdriver.common.by import By
from .base_page_with_driver import BasePageWithDriver
from controls.button import Button
from controls.selectbox import SelectBox
from controls.textbox import TextBox


class GaragePage(BasePageWithDriver):
    def __init__(self):
        super().__init__()

    def get_my_profile_button(self):
        return Button(self._driver.find_element(By.ID, "userNavDropdown"))

    def get_add_car_button(self):
        return Button(self._driver.find_element(By.XPATH, "//button[text()='Add car']"))

    def get_modify_car_button(self):
        return Button(self._driver.find_element(By.XPATH, "//button[contains(@class,'car_edit')]"))

    def get_form_add_car_button(self):
        return Button(self._driver.find_element(By.XPATH, "//button[text()='Add']"))

    def get_form_save_car_button(self):
        return Button(self._driver.find_element(By.XPATH, "//button[text()='Save']"))

    def get_form_remove_car_button(self):
        return Button(self._driver.find_element(By.XPATH, "//button[text()='Remove car']"))

    def get_form_remove_car_confirm_button(self):
        return Button(self._driver.find_element(By.XPATH, "//button[text()='Remove']"))

    def get_form_brand_field(self):
        return SelectBox(self._driver.find_element(By.ID, "addCarBrand"))

    def get_form_model_field(self):
        return SelectBox(self._driver.find_element(By.ID, "addCarModel"))

    def get_form_mileage_field(self):
        return TextBox(self._driver.find_element(By.ID, "addCarMileage"))



    # 5 methods here. 2 for buttons (add car / add [on the form]), 3 inputs/selectboxes (brand,model,mileage)
