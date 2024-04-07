import pandas as pd
from database import get_database
from pymongo import UpdateOne
from dotenv import load_dotenv
import os


def get_data_from_csv():
    load_dotenv()
    FILE_PATH = os.getenv("CSV_FILE_PATH")
    data = pd.read_csv(FILE_PATH)
    return data


def insert_data_into_collection(collection_name, data):
    db = get_database()
    collection = db[collection_name]
    records = data.to_dict(orient='records')
    # To clean special characters from field names
    cleaned_records = [{key.strip(): value for key, value in record.items()} for record in records]

    bulk_operations = []
    for record in cleaned_records:
        # To check if the record already exists in the collection
        existing_record = collection.find_one(record)
        if existing_record is None:
            # To create an update operation for each record.
            bulk_operations.append(UpdateOne(
                record,  # Use the entire record as the search filter
                {'$set': record},  # Define the data of the record to insert or update
                upsert=True  # Specify upsert=True to insert new records or update existing records.
            ))
        else:
            print(f"The record {record} already exist in the collection.")

    try:
        if bulk_operations:
            # Execute batch update operations only if there are new insertions.
            result = collection.bulk_write(bulk_operations, ordered=False)
            print(
                f"{result.upserted_count + result.modified_count} records have been inserted/updated in the collection.")
        else:
            print("There are no new records to insert.")
    except Exception as e:
        print(f"Error inserting/updating records: {e}")
