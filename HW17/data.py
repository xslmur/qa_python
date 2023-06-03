from pymongo import MongoClient
import json


class PetAboutModel:
    def __init__(self, favourite_toy: str,  minnie_mouse: str):
        self.favourite_toy: str = favourite_toy
        self.minnie_mouse: str = minnie_mouse

    @staticmethod
    def from_json(json_data: dict):
        return PetAboutModel(
            json_data["favourite_toy"],
            json_data["temperament"])

    def __repr__(self):
        return f"PetAboutModel(favourite_toy:{self.favourite_toy}, minnie_mouse:{self.minnie_mouse})"


class PetModel:
    def __init__(self, pet_name: str, pet_age: float, about_pet: PetAboutModel):
        self.pet_name: str = pet_name
        self.pet_age: float = pet_age
        self.about_pet: PetAboutModel = about_pet

    @staticmethod
    def from_json(json_data: dict):
        return PetModel(
            json_data["pet_name"],
            json_data["pet_age"],
            PetAboutModel.from_json(json_data["about_pet"]))

    def __repr__(self):
        return f"PetModel(pet_name:{self.pet_name}, pet_age:{self.pet_age}, about:{self.about_pet!r})"


class PersonModel:
    def __init__(self, _id: str, name: str, email: str, age: int, pets: list[PetModel]):
        self._id = _id
        self.name: str = name
        self.email: str = email
        self.age: int = age
        self.pets: list[PetModel] = pets

    @staticmethod
    def from_json(json_data: dict):
        return PersonModel(
            json_data["_id"],
            json_data["name"],
            json_data["email"],
            json_data["age"],
            [PetModel.from_json(pet_json_data) for pet_json_data in json_data["pets"]]
        )

    def __repr__(self):
        return f"PersonModel(id:{self._id}, name:{self.name}, email:{self.email}, age:{self.age}, pets:{self.pets!r}))"


def insert_from_file_to_mongodb(file_name, collection):
    with open(file_name) as file:
        file_data = json.load(file)
    print(f"> insert json from the file '{file_name}' to mongodb collection '{collection.name}':\n{file_data}")
    collection.insert_many(file_data)


def read_from_mongodb_to_model(collection, document_filter):
    print(f"\n> read from mongodb collection '{collection.name}' and parse to the model by filter:", document_filter)

    person_json_data = collection.find_one(document_filter)
    print('json:\n', person_json_data)

    person = PersonModel.from_json(person_json_data)
    print('person:\n', person)


def clear_mongodb(collection, document_filter):
    print("\n> remove from mongodb collection '{collection.name}' by filter:", document_filter)
    collection.delete_many(document_filter)


if __name__ == "__main__":
    mongo_client = MongoClient("mongodb://localhost:27017")
    db = mongo_client["hillel_db"]
    db_collection = db["my_collection_3"]

    doc_filter = {"name": "Cheadle Yorkshire"}

    insert_from_file_to_mongodb('data.json', db_collection)
    read_from_mongodb_to_model(db_collection, doc_filter)
    clear_mongodb(db_collection, doc_filter)
