#from pymongo import MongoClient
#from os import getenv
#
#
#class BnFMongoManager:
#
#    def __init__(self):
#        self.__client = MongoClient(getenv("MONGO_CONNECTION_STRING", ""))


from pymongo import MongoClient

# Connect to MongoDB running on your laptop
client = MongoClient("mongodb://localhost:27017")

# Your database
db = client["bnfweb"]

# Your theatres table
theatres_collection = db["theatres"]

# Your slots table
slots_collection = db["slots"]
