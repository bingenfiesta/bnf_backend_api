
from pymongo import MongoClient
from os import getenv

def main():
    cs = getenv("MONGO_CONNECTION_STRING")
    client = MongoClient(cs, serverSelectionTimeoutMS=5000)
    try:
        client.admin.command("ping")
        print("OK")
    except Exception as e:
        print("Failed:", e)


if __name__ == "__main__":
    main()