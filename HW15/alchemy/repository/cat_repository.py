from alchemy.models.cat_model import CatModel
from alchemy.session import session
from sqlalchemy import delete, insert


class CatRepository:
    def __init__(self):
        self.__session = session
        self.__model = CatModel

    def get_all(self) -> list[CatModel]:
        return self.__session.query(self.__model).all()

    def get_item_by_id(self, cat_id):
        return self.__session.get(self.__model, cat_id)

    def add_item(self, **kwargs):
        return self.__session.scalar(insert(CatModel).returning(CatModel), kwargs)

    def update_item(self, cat: CatModel):
        return self.__session.add(cat)

    def remove_item(self, cat: CatModel):
        return self.__session.delete(cat)

    def remove_item_by_id(self, cat_id: int) -> None:
        # cat = self.__session.get(self.__model, cat_id)
        # self.__session.delete(cat)
        self.__session.execute(delete(self.__model).where(self.__model.id == cat_id))
