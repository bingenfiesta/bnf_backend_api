from pymongo import MongoClient
from os import getenv


class BnFMongoManager:

    def __init__(self, collection_name: str):
        self.__client = MongoClient(getenv("MONGO_CONNECTION_STRING", ""))
        self.__db = self.__client[getenv("MONGO_DB_NAME", "BNF")]
        self.collection_name = collection_name

    def add_records(self):
        self.collection = self.__db[self.collection_name]
        
