from database import create_database_if_not_exists, create_collection
from insert_data import get_data_from_csv, insert_data_into_collection
from dotenv import load_dotenv
import os


def main():
    load_dotenv()
    DATABASE_NAME = os.getenv("MONGODB_DATABASE")
    create_database_if_not_exists(DATABASE_NAME)

    COLLECTION_NAME = os.getenv("MONGODB_COLLECTION")
    create_collection(COLLECTION_NAME)

    data = get_data_from_csv()
    insert_data_into_collection(COLLECTION_NAME, data)


if __name__ == '__main__':
    main()
