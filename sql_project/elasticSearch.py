import sqlite3 as sql
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from drivingInstructor import *


# Connect to Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# Function to create an Elasticsearch index and define mapping
def create_elasticsearch_index(index_name):
    mapping = {
        "mappings": {
            "properties": {
                "Name": {"type": "text"},
                "Email": {"type": "text"},
                "Phone_Number": {"type": "keyword"},
                "Distance": {"type": "text"},
                "Postcode": {"type": "keyword"},
            }
        }
    }
    es.indices.create(index=index_name, body=mapping, ignore=400)

# Function to bulk index data into Elasticsearch
def bulk_index_data(index_name, data):
    actions = [
        {
            "_op_type": "index",
            "_index": index_name,
            "_id": str(row[0]),  # Use a unique identifier as the document ID
            "_source": {
                "Name": row[1],
                "Email": row[2],
                "Phone_Number": row[3],
                "Distance": row[4],
                "Postcode": row[5],
            }
        }
        for row in data
    ]
    bulk(es, actions)

# Connect to SQLite and create tables
dbconnect = sql.connect('SQL/sql_project/drivingInstructors.db')
dbcursor = dbconnect.cursor()

# Create table 'B' if not exists
dbcursor.execute('''
    CREATE TABLE IF NOT EXISTS B (
        ID INTEGER PRIMARY KEY,
        Name VARCHAR(255),
        Email VARCHAR(255),
        Phone_Number VARCHAR(15),
        Distance VARCHAR(20),
        Postcode VARCHAR(10)
    )
''')

# Create table 'BA' if not exists
dbcursor.execute('''
    CREATE TABLE IF NOT EXISTS BA (
        ID INTEGER PRIMARY KEY,
        Name VARCHAR(255),
        Email VARCHAR(255),
        Phone_Number VARCHAR(15),
        Distance VARCHAR(20),
        Postcode VARCHAR(10)
    )
''')

# Commit changes to SQLite
dbconnect.commit()

# Create Elasticsearch index for 'B'
create_elasticsearch_index("driving_instructors_b")

# Fetch existing data from SQLite table 'B' and bulk index into Elasticsearch
dbcursor.execute("SELECT * FROM B")
existing_data_B = dbcursor.fetchall()
bulk_index_data("driving_instructors_b", existing_data_B)

# Create Elasticsearch index for 'BA'
create_elasticsearch_index("driving_instructors_ba")

# Fetch existing data from SQLite table 'BA' and bulk index into Elasticsearch
dbcursor.execute("SELECT * FROM BA")
existing_data_BA = dbcursor.fetchall()
bulk_index_data("driving_instructors_ba", existing_data_BA)

# Close SQLite connection
dbconnect.close()
