# CSV Data Importer to MongoDB

This project consists of a Python script that allows loading a dataset from a CSV file into a MongoDB database. The script creates a database and a collection in MongoDB, then inserts the records from the CSV file into the collection, avoiding the insertion of duplicate records.

## Usage

1. **Dependencies Installation:**
   
   Before running the script, make sure you have the following dependencies installed:

   ```bash
   pip install pandas pymongo python-dotenv

2. **Environment Configuration:**
   ```bash
   MONGODB_CONNECTION_STRING="mongodb://user:pass@localhost/"
   MONGODB_DATABASE="YOUR_DATABASE"
   MONGODB_COLLECTION="YOUR_COLLECTION"

3. **Execute script:**
  Execute the main.py script to load the data from the CSV file to MongoDB:
  
   ```bash
   python main.py

## Usage

The dataset used is located in the file **annual_cause_death_numbers.csv**. It contains statistics of deaths due to various causes in different countries and years.

This dataset was obtained from [Kaggle](https://www.kaggle.com/), an online platform for machine learning and data science. The file is licensed under CC0 Public Domain, which means it is in the public domain and can be used for any purpose without restrictions.

Here's an example of a record from the **annual_cause_death_numbers.csv** file:

| Field                               | Value     |
|-------------------------------------|-----------|
| Entity         | Afghanistan |
| Code           | AFG         |
| Year           | 1990        |
| Meningitis fatalities | 2159 |
| Dementia fatalities | 1116 |
| Parkinson s fatalities | 371 |
| Nutritional deficiency fatalities | 2087 |
| Malaria fatalities | 93 |
| ...                                 | ...       |
