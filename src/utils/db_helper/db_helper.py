from os import getenv

from bson.objectid import ObjectId
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


class BnFMongoManager:

    def __init__(self, collection_name: str) -> None:
        self.__client = MongoClient(getenv("MONGO_CONNECTION_STRING", ""))
        self.__db = self.__client[getenv("MONGO_DB_NAME", "BNF")]
        self.collection = self.__db[collection_name]

    def get_record(self, id: str):
        result = self.collection.find_one({"_id": ObjectId(id)})
        result["_id"] = str(result['_id'])
        return result

    def insert_record(self, insertion_data: dict) -> str:
        result = self.collection.insert_one(insertion_data)
        return str(result.inserted_id)

    def update_record(self, id: str, updates: dict):
        update_operation = {"$set": updates}
        result = self.collection.update_one({"_id": ObjectId(id)}, update_operation)
        return result.modified_count

    def delete_record(self, id: str):
        return self.update_record({ "delete": "true" }) 

    def hard_delete_record(self, id: str):
        result = self.collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count

    def get_records(self, skip_count=0, page_size=50, filter={}):
        result = self.collection.find(filter).sort('_id', 1).skip(skip_count).limit(page_size)
        return list(result)