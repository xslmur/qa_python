import requests
import time

from driver import Driver

from models.user import UserLoginData, User
from models.cars import CarData, Cars
from models.brands import Brands
from models.models import Models

from pages.login_page import LoginPage
from pages.garage_page import GaragePage

API_BASE = 'https://qauto2.forstudy.space/api/'
WEB_UI_URL = 'https://guest:welcome2qauto@qauto2.forstudy.space/'


class TestCarsAPI:
    def setup_class(self):
        self.session = requests.session()

        user_to_login = UserLoginData("test@tesster.com", "Qwerty12345", False)
        self.user = User(API_BASE, self.session, 'TestName', 'TestLastName', user_to_login)
        self.cars = Cars(API_BASE, self.session)

        self.driver = Driver.get_chrome_driver()
        self.login_page = LoginPage()
        self.garage_page = GaragePage()

        # create user via API
        self.user.register()
        # login API
        ret = self.user.login()
        assert ret['status'] == 'ok'

        # retrieve brands and models mappings
        self.car_brands = Brands(API_BASE, self.session)
        self.car_models = Models(API_BASE, self.session)

        # login into web UI (garage page)
        self.driver.get(WEB_UI_URL)
        self.login_page.do_login(self.user.user_login.email, self.user.user_login.password)
        assert self.garage_page.get_my_profile_button().is_displayed()

    # def setup_method(self):
    #     self.driver.get(WEB_UI_URL)
    #     self.login_page.do_login(self.user.user_login.email, self.user.user_login.password)
    #     assert self.garage_page.get_my_profile_button().is_displayed()

    def test_auto_create(self):
        car_data = CarData({
            'carBrandId': 3,  # Ford
            'carModelId': 11,  # Fiesta
            'mileage': 8000
        })

        car_brand_name = self.car_brands.get_brand_by_id(car_data.carBrandId)
        car_model_name = self.car_models.get_model_by_id(car_data.carBrandId, car_data.carModelId)

        # here we already performed login (did it in the setup method)

        # click 'add Car' button
        self.garage_page.get_add_car_button().click()
        # fill in fields
        self.garage_page.get_form_brand_field().select_by_visible_text(car_brand_name)
        self.garage_page.get_form_model_field().select_by_visible_text(car_model_name)
        self.garage_page.get_form_mileage_field().fill_field(car_data.mileage)
        # click button Add
        self.garage_page.get_form_add_car_button().click()

        time.sleep(0.5)

        # get cars via API
        cars = self.cars.get()

        # cleanup
        self.cars.delete_cars(cars)

        # ensure it's the only car in the garage
        assert len(cars) == 1
        car = cars[0]
        # verify created car data
        assert car.data == car_data

    def test_auto_modify(self):
        # create car by API
        car_data = CarData({
            'carBrandId': 3,  # Ford
            'carModelId': 11,  # Fiesta
            'mileage': 8000
        })
        self.cars.create(car_data)

        # modify car in web ui
        car_data.mileage = 10000  # 8000 -> 10000
        self.driver.refresh()
        # click 'modify car' button
        self.garage_page.get_modify_car_button().click()
        # fill in mileage with the new value
        self.garage_page.get_form_mileage_field().fill_field(car_data.mileage)
        # click 'save' button
        self.garage_page.get_form_save_car_button().click()

        time.sleep(0.5)

        # verify car is modified via API
        cars = self.cars.get()

        # cleanup
        self.cars.delete_cars(cars)

        assert len(cars) == 1  # check for single car
        car = cars[0]
        # print(car.data.__dict__)
        # print(car_data.__dict__)
        assert car.data == car_data

    def test_auto_delete(self):
        # create car by API
        car_data = CarData({
            'carBrandId': 3,  # Ford
            'carModelId': 11,  # Fiesta
            'mileage': 8000
        })
        self.cars.create(car_data)

        self.driver.refresh()

        # remove car by web UI
        self.garage_page.get_modify_car_button().click()
        self.garage_page.get_form_remove_car_button().click()
        self.garage_page.get_form_remove_car_confirm_button().click()

        time.sleep(0.5)

        # verify it was removed using API
        cars = self.cars.get()
        assert len(cars) == 0

    def teardown_class(self):
        self.user.delete()
