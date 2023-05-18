import requests
import time
import allure

from driver import Driver

# from models.user import UserLoginData, User
from models.user import UserLoginData
from facades.user_facade import UserFacade
# from models.cars import CarData, Cars
from models.cars import CarData
from facades.cars_facade import CarsFacade
# from models.brands import Brands
from facades.car_brands_facade import CarBrandsFacade
# from models.models import Models
from facades.car_models_facade import CarModelsFacade

# from pages.login_page import LoginPage
from facades.login_facade import LoginFacade
# from pages.garage_page import GaragePage
from facades.garage_facade import GarageFacade

API_BASE = 'https://qauto2.forstudy.space/api/'
WEB_UI_URL = 'https://guest:welcome2qauto@qauto2.forstudy.space/'


class TestCarsUI:
    def setup_class(self):
        self.session = requests.session()

        user_to_login = UserLoginData("test@tesster.com", "Qwerty12345", False)
        self.user_facade = UserFacade(API_BASE, self.session, 'TestName', 'TestLastName', user_to_login)
        self.cars_facade = CarsFacade(API_BASE, self.session)

        self.driver = Driver.get_chrome_driver()
        self.login_facade = LoginFacade()
        self.garage_facade = GarageFacade()

        # create user via API
        self.user_facade.register()
        # login API
        ret = self.user_facade.login()
        assert ret['status'] == 'ok'

        # retrieve brands and models mappings
        self.car_brands_facade = CarBrandsFacade(API_BASE, self.session)
        self.car_models_facade = CarModelsFacade(API_BASE, self.session)

        # login into web UI (garage page)
        self.driver.get(WEB_UI_URL)
        self.login_facade.do_login(self.user_facade.user_login.email, self.user_facade.user_login.password)
        assert self.garage_facade.get_my_profile_button().is_displayed()

    @allure.description("create car via WEB UI and check it values via API")
    @allure.issue("https://qauto2.forstudy.space/garage/", "Test issue: WEB UI Car creation issues")
    def test_auto_create(self):
        car_data = CarData({
            'carBrandId': 3,  # Ford
            'carModelId': 11,  # Fiesta
            'mileage': 8000
        })

        car_brand_name = self.car_brands_facade.get_brand_by_id(car_data.carBrandId)
        car_model_name = self.car_models_facade.get_model_by_id(car_data.carBrandId, car_data.carModelId)

        # here we already performed login (did it in the setup method)

        # click 'add Car' button
        self.garage_facade.click_add_car_button()
        # fill in fields
        self.garage_facade.select_car_brand(car_brand_name)
        self.garage_facade.select_car_model(car_model_name)
        self.garage_facade.fill_car_mileage(car_data.mileage)
        # click button Add
        self.garage_facade.click_form_add_car_button()

        time.sleep(0.5)

        # get cars via API
        cars = self.cars_facade.get()

        # cleanup
        self.cars_facade.delete_cars(cars)

        # ensure it's the only car in the garage
        assert len(cars) == 1
        car = cars[0]
        # verify created car data
        assert car.data == car_data

    @allure.description("modify Car via UI and then verify it updated via API")
    @allure.issue("https://qauto2.forstudy.space/garage/", "Test issue: WEB UI Car modification issues")
    def test_auto_modify(self):
        # create car by API
        car_data = CarData({
            'carBrandId': 3,  # Ford
            'carModelId': 11,  # Fiesta
            'mileage': 8000
        })
        self.cars_facade.create(car_data)

        # modify car in web ui
        car_data.mileage = 10000  # 8000 -> 10000
        self.driver.refresh()
        # click 'modify car' button
        self.garage_facade.click_modify_car_button()
        # fill in mileage with the new value
        self.garage_facade.fill_car_mileage(car_data.mileage)
        # click 'save' button
        self.garage_facade.click_form_save_car_button()

        time.sleep(0.5)

        # verify car is modified via API
        cars = self.cars_facade.get()

        # cleanup
        self.cars_facade.delete_cars(cars)

        assert len(cars) == 1  # check for single car
        car = cars[0]
        # print(car.data.__dict__)
        # print(car_data.__dict__)
        assert car.data == car_data

    @allure.description("create car via APi. delete car via WEB UI and check it removed via API")
    @allure.issue("https://qauto2.forstudy.space/garage/", "Test issue: WEB UI Car deletion issues")
    def test_auto_delete(self):
        # create car by API
        car_data = CarData({
            'carBrandId': 3,  # Ford
            'carModelId': 11,  # Fiesta
            'mileage': 8000
        })
        self.cars_facade.create(car_data)

        self.driver.refresh()

        # remove car by web UI
        self.garage_facade.click_modify_car_button()
        self.garage_facade.click_form_remove_car_button()
        self.garage_facade.click_form_remove_car_confirm_button()

        time.sleep(0.5)

        # verify it was removed using API
        cars = self.cars_facade.get()
        assert len(cars) == 0

    def teardown_method(self):
        screen_name_using_current_time = time.strftime("%Y%m%d-%H%M%S")
        allure.attach(self.driver.get_screenshot_as_png(), name=screen_name_using_current_time)

    def teardown_class(self):
        self.user_facade.delete()
