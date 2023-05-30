from pony.orm import db_session, select


class BaseRepository:
    def __init__(self, model):
        self.__model = model

    @db_session
    def get_by_id(self, entry_id):
        entity = self.__model.get(lambda r: r.id == entry_id)
        return entity

    @db_session
    def delete_by_id(self, entry_id):
        entity = self.get_by_id(entry_id)
        entity.delete()
