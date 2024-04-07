import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()


def get_client():
    CONNECTION_STRING = os.getenv("MONGODB_CONNECTION_STRING")
    client = MongoClient(CONNECTION_STRING)
    return client


def get_database():
    client = get_client()
    DATABASE_NAME = os.getenv("MONGODB_DATABASE")
    db = client[DATABASE_NAME]
    return db


def create_database_if_not_exists(database_name):
    client = get_client()
    existing_databases = client.list_database_names()
    if database_name in existing_databases:
        print(f"The database '{database_name}' already exist.")
        return
    else:
        db = client[database_name]
        print(f"The database '{database_name}' has been created.")
        return


def create_collection(collection_name):
    db = get_database()
    if collection_name in db.list_collection_names():
        print(f"The collection '{collection_name}' already exist.")
        return
    else:
        db.create_collection(collection_name)
        print(f"The collection '{collection_name}' has been created.")
