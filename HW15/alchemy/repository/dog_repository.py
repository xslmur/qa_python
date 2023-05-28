from alchemy.models.dog_model import DogModel
from alchemy.session import session
from sqlalchemy import delete, insert


class DogRepository:
    def __init__(self):
        self.__session = session
        self.__model = DogModel

    def get_all(self):
        return self.__session.query(self.__model).all()

    def get_item_by_id(self, dog_id):
        return self.__session.get(self.__model, dog_id)

    def add_item(self, **kwargs):
        return self.__session.scalar(insert(DogModel).returning(DogModel), kwargs)

    def update_item(self, dog: DogModel):
        return self.__session.add(dog)

    def remove_item(self, dog: DogModel):
        return self.__session.delete(dog)

    def remove_item_by_id(self, dog_id: int):
        # dog = self.__session.get(self.__model, dog_id)
        # self.__session.delete(dog)
        self.__session.execute(delete(self.__model).where(self.__model.id == dog_id))
