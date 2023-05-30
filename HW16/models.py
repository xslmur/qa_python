from pony.orm import Database, PrimaryKey, Optional, Required, Set
from db import db


class Cat(db.Entity):
    _table_ = "cats"
    id = PrimaryKey(int, auto=True)
    name = Required(str, 50)
    breed = Required(str, 50)
    age = Required(int)
    owner = Required(str, 50)

    dogs = Set('Dog', reverse='owner_cat')

    def __repr__(self):
        return f"Cat(ID: {self.id}, Name: {self.name}, Breed: {self.breed}, Age: {self.age}, Owner: {self.owner})"


class Dog(db.Entity):
    _table_ = "dogs"
    id = PrimaryKey(int, auto=True)
    name = Required(str, 50)
    breed = Required(str, 50)
    age = Required(int)
    owner = Required(str, 50)
    owner_cat = Optional(Cat, column='owner_cat_id', reverse='dogs')

    def __repr__(self):
        return f"Dog(ID: {self.id}, Name: {self.name}, Breed: {self.breed}, Age: {self.age}, Owner: {self.owner})"


db.generate_mapping(create_tables=False)
# db.generate_mapping(create_tables=True)
