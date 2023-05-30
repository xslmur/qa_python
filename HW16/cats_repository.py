from pony.orm import db_session, select
from base_repository import BaseRepository
from models import Cat


class CatsRepository(BaseRepository):
    def __init__(self):
        super().__init__(Cat)

    @db_session
    def get_all_by_lambda(self):
        cats_query = Cat.select(lambda cat: cat)
        return cats_query.prefetch(Cat.dogs)[:]

    @db_session
    def get_all_by_for(self):
        cats_query = select(c for c in Cat)
        return cats_query.prefetch(Cat.dogs)[:]








