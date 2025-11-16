from pymongo import MongoClient
from os import getenv


class BnFMongoManager:

    def __init__(self):
        self.__client = MongoClient(getenv("MONGO_CONNECTION_STRING", ""))
        
