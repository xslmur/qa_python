from pony.orm import db_session, select, left_join
from base_repository import BaseRepository
from models import Dog


class DogsRepository(BaseRepository):
    def __init__(self):
        super().__init__(Dog)

    @db_session
    def get_all_by_lambda(self):
        cat = Dog.select(lambda role: role)
        return cat.prefetch(Dog.owner_cat).page(1).to_list()

    @db_session
    def get_all_by_for(self):
        cats_query = select(c for c in Dog)
        return cats_query.prefetch(Dog.owner_cat)[:]
