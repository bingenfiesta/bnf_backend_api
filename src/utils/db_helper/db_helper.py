from os import getenv

from bson.objectid import ObjectId
from pymongo import MongoClient
from dotenv import load_dotenv
import json

load_dotenv()


class BnFMongoManager:

    def __init__(self, collection_name: str) -> None:
        self.__client = MongoClient(getenv("MONGO_CONNECTION_STRING", ""))
        self.__db = self.__client[getenv("MONGO_DB_NAME", "BNF")]
        self.collection = self.__db[collection_name]

    def get_record(self, id: str):
        result = self.collection.find_one({"_id": ObjectId(id)})
        if not result:
            return None
        result["_id"] = str(result["_id"])
        return result

    def insert_record(self, insertion_data: dict) -> str:
        # Accept JSON string or dict
        if isinstance(insertion_data, str):
            try:
                insertion_data = json.loads(insertion_data)
            except Exception:
                raise ValueError("insertion_data must be a dict or JSON string")

        result = self.collection.insert_one(insertion_data)
        return str(result.inserted_id)

    def update_record(self, id: str, updates: dict):
        update_operation = {"$set": updates}
        result = self.collection.update_one({"_id": ObjectId(id)}, update_operation)
        return result.modified_count

    def delete_record(self, id: str):
        # Soft delete: set delete flag to true
        return self.update_record(id, {"delete": True}) 

    def hard_delete_record(self, id: str):
        result = self.collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count

    def get_records(self, skip_count=0, page_size=50, filter={}):
        if filter is None:
            filter = {}
        cursor = self.collection.find(filter).sort('_id', 1).skip(skip_count).limit(page_size)
        docs = []
        for d in cursor:
            d["_id"] = str(d["_id"])
            docs.append(d)
        return docs