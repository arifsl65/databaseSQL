import sqlite3 as sql

def search_across_tables(field_number, search_value):
    # Define a dictionary to map user input to the corresponding field in the table
    field_mapping = {
        1: 'Name',
        2: 'Email',
        3: 'Phone_Number',
        4: 'Distance',
        5: 'Postcode'
    }

    # Connect to the database and create a cursor
    dbconnect = sql.connect('SQL/sql_project/drivingInstructors.db')
    dbcursor = dbconnect.cursor()

    # Fetch the list of tables in the database
    dbcursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = dbcursor.fetchall()

    # Iterate over the tables and perform the search
    for table in tables:
        table_name = table[0]

        # Define the SQL query based on user input
        query = f'SELECT * FROM {table_name} WHERE {field_mapping[field_number]} = ?'

        # Execute the query with the provided search value
        dbcursor.execute(query, (search_value,))

        # Fetch all the results
        results = dbcursor.fetchall()

        # Print the results
        if results:
            print(f"Results for {field_mapping[field_number]} = {search_value} in table {table_name}:")
            for row in results:
                print(row)
        else:
            print(f"No results found for {field_mapping[field_number]} = {search_value} in table {table_name}")

    # Close the database connection
    dbconnect.close()

# Take user inputs
field_number = int(input("Enter the field number to search (1 Name, 2 Email, 3 Phone_Number, 4 Distance, 5 Postcode): "))
search_value = input("Enter the value to search for: ")

# Perform the search across all tables
search_across_tables(field_number, search_value)
