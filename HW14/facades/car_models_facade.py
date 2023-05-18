import allure
from models.models import Models


class CarModelsFacade(Models):
    @allure.step("retrieve car models via API")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @allure.step("resolve car model name by id")
    def get_brand_by_id(self, brand_id):
        return super().get_brand_by_id(brand_id)