from cats_repository import CatsRepository
from dogs_repository import DogsRepository


def print_cat(cat_data):
    print(cat_data)
    for dog_data in cat_data.dogs:
        print('   owned dog: ', dog_data)


def print_dog(dog_data):
    print(dog_data)
    print('  owner cat: ', dog_data.owner_cat)


if __name__ == '__main__':
    cats_repo = CatsRepository()
    dogs_repo = DogsRepository()

    print('cats = cats_repo.get_all_by_lambda()')
    cats = cats_repo.get_all_by_lambda()
    for cat in cats:
        print_cat(cat)

    print('\ncats = cats_repo.get_all_by_for()')
    cats = cats_repo.get_all_by_for()
    for cat in cats:
        print_cat(cat)

    print('\ncat = cats_repo.get_by_id(cats[0].id)')
    cat = cats_repo.get_by_id(cats[0].id)
    print(cat)

    print('\ndogs = dogs_repo.get_all_by_lambda()')
    dogs = dogs_repo.get_all_by_lambda()
    for dog in dogs:
        print_dog(dog)

    print('\ndogs = dogs_repo.get_all_by_for()')
    dogs = dogs_repo.get_all_by_for()
    for dog in dogs:
        print_dog(dog)
