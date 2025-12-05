from pymongo import MongoClient
from os import getenv
from bson.objectid import ObjectId


class BnFMongoManager:

    def __init__(self, collection_name: str) -> None:
        self.__client = MongoClient(getenv("MONGO_CONNECTION_STRING", ""))
        self.__db = self.__client[getenv("MONGO_DB_NAME", "BNF")]
        self.collection = self.__db[collection_name]

    def get_record(self, id: str):
        result = self.collection.find_one({"_id": ObjectId(id)})
        return result

    def insert_record(self, insertion_data: dict) -> str:
        result = self.collection.insert_one(insertion_data)
        return str(result.inserted_id)

    def update_record(self, id: str, updates: dict):
        update_operation = {"$set": updates}
        result = self.collection.update_one({"_id": ObjectId(id)}, update_operation)
        return result.modified_count

    def delete_record(self, id: str):
        result = self.collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count
