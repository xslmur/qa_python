from pymongo import MongoClient

mongo_client = MongoClient("mongodb://localhost:27017")
db = mongo_client["hillel_db"]
collection = db["my_collection"]
