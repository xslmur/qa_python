import requests

#{'id': 95935,
# 'carBrandId': 3,
# 'carModelId': 11,
# 'initialMileage': 8000,
# 'updatedMileageAt': '2023-05-15T16:58:41.000Z',
# 'carCreatedAt': '2023-05-15T16:58:41.000Z',
# 'mileage': 8000,
# 'brand': 'Ford',
# 'model': 'Fiesta',
# 'logo': 'ford.png'}


class CarData:
    def __init__(self, data):
        self.carBrandId = data['carBrandId']
        self.carModelId = data['carModelId']
        self.mileage = data['mileage']
        # TODO: add more fields

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return 'CarData {}'.format(self.__dict__)


class Car:
    def __init__(self, data):
        self.id = data['id']
        self.data = CarData(data)

    def __repr__(self):
        return 'Car id:{}, data:{}'.format(
            self.id, self.data.__dict__
        )


class Cars:
    CARS_PATH = 'cars'

    def __init__(self, api_base: str, session: requests.sessions):
        self.api_base = api_base
        self.session = session

    def get(self) -> list[Car]:
        ret = self.session.get(self.api_base + self.CARS_PATH)
        assert ret.status_code == 200
        ret_json = ret.json()
        assert ret_json['status'] == 'ok'
        cars = []
        for car_json in ret_json['data']:
            cars.append(Car(car_json))
        return cars

    def create(self, data: CarData) -> Car:
        ret = self.session.post(self.api_base + self.CARS_PATH, json=data.__dict__)
        assert ret.status_code == 201
        ret_json = ret.json()
        assert ret_json['status'] == 'ok'
        return Car(ret_json['data'])

    def delete_cars(self, cars: list[Car]):
        for car in cars:
            self.session.delete(self.api_base + self.CARS_PATH + '/{}'.format(car.id))

    def delete_all_cars(self):
        self.delete_cars(self.get())
