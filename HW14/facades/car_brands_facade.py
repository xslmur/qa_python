import allure
from models.brands import Brands


class CarBrandsFacade(Brands):
    @allure.step("retrieve car brands via API")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @allure.step("resolve car brand name by id")
    def get_brand_by_id(self, brand_id):
        return super().get_brand_by_id(brand_id)
