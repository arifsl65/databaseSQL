import sqlite3 as sql

def search_across_tables(field_number, search_value):
    # Map the user's field number to the actual field name
    field_mapping = {
        1: 'Name',
        2: 'Email',
        3: 'Phone_Number',
        4: 'Distance',
        5: 'Postcode'
    }

    # Connect to the SQLite database
    dbconnect = sql.connect('SQL/sql_project/drivingInstructors.db')
    dbcursor = dbconnect.cursor()

    # Get the list of tables in the database
    dbcursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = dbcursor.fetchall()

    # Dictionary to store records from each table
    records = {}

    # Iterate through each table and retrieve records for the specified field
    for table in tables:
        table_name = table[0]
        field_name = field_mapping[field_number]
        
        # Use LOWER function for case-insensitive comparison (for "Name", "Email", and "Postcode" fields)
        if field_name in ['Name', 'Email', 'Postcode']:
            query = f"SELECT * FROM {table_name} WHERE LOWER({field_name}) LIKE ?"
        else:
            query = f"SELECT * FROM {table_name} WHERE {field_name} LIKE ?"
            
        dbcursor.execute(query, (f"%{search_value.lower()}%",))
        records[table_name] = dbcursor.fetchall()

    # Close the database connection
    dbconnect.close()

    return records, field_mapping[field_number]

def display_records(records, field_name, search_value):
    # Display the records to the user
    for table_name, record_list in records.items():
        print(f"\nRecords in table '{table_name}' matching '{field_name}' and '{search_value}':")
        for record in record_list:
            print(record)

# Get the field number to search from the user
field_number = int(input("Enter the field number to search (1 Name, 2 Email, 3 Phone_Number, 4 Distance, 5 Postcode): "))

# Get the value to search for from the user
search_value = input("Enter the value to search for: ")

# Perform the search and display the records
records, field_name = search_across_tables(field_number, search_value)
display_records(records, field_name, search_value)

if __name__ == "__main__":
    search_across_tables()
