import requests


class Models:
    def __init__(self, api_base, session):
        self.models = session.get(api_base + 'cars/models').json()['data']

    def get_model_by_id(self, brand_id, model_id):
        for model in self.models:
            if model['carBrandId'] == brand_id and model['id'] == model_id:
                return model['title']
        return None
