import allure
from models.cars import Cars, Car, CarData


class CarsFacade(Cars):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @allure.step("retreive cars via API")
    def get(self) -> list[Car]:
        return super().get()

    @allure.step("create car via API")
    def create(self, data: CarData) -> Car:
        return super().create(data)

    @allure.step("delete cars via API")
    def delete_cars(self, cars: list[Car]):
        return super().delete_cars(cars)

    @allure.step("delete ALL cars via API")
    def delete_all_cars(self):
        return super().delete_cars()
