from alchemy.repository.cat_repository import CatRepository
from alchemy.repository.dog_repository import DogRepository

from alchemy.models.cat_model import CatModel
# from alchemy.models.dog_model import DogModel
from sqlalchemy import select

from alchemy.session import session

if __name__ == "__main__":
    print('db data:')
    for cat in session.scalars(select(CatModel)):
        print(cat)
        for dog in cat.dogs:
            print('..', dog)

    cats = CatRepository()
    dogs = DogRepository()

    print('\ncats.get_all():')
    for cat in cats.get_all():
        print(cat)

    print('\ncats.get_item_by_id(1):')
    #save to restore later
    cat = cats.get_item_by_id(1)
    print(cat)

    print("\ncat = cats.add_item(name='test', breed='test', age=42, owner='test')")
    cat = cats.add_item(name='test', breed='test', age=42, owner='test')
    print(cat)

    cat.age += 1
    print('\ncats.update_item(cat)')
    cats.update_item(cat)
    session.commit()

    print('\ncats.remove_item(cat)')
    cats.remove_item(cat)
    session.commit()

    print("\ncat = cats.add_item(name='test2', breed='test2', age=42, owner='test2')")
    cat = cats.add_item(name='test2', breed='test2', age=42, owner='test2')
    print(cat)

    print("\ncats.remove_item_by_id(cat.id)")
    cats.remove_item_by_id(cat.id)
