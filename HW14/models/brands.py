import requests


class Brands:
    def __init__(self, api_base, session):
        self.brands = session.get(api_base + 'cars/brands').json()['data']

    def get_brand_by_id(self, brand_id):
        for brand in self.brands:
            if brand['id'] == brand_id:
                return brand['title']
        return None
