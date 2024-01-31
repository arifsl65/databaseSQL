import sqlite3 as sql

def get_records_by_name(name_to_update):
    # Convert the user input to lowercase (or uppercase)
    name_to_update_lower = name_to_update.lower()

    # Connect to the SQLite database
    with sql.connect('SQL/sql_project/drivingInstructors.db') as dbconnect:
        dbcursor = dbconnect.cursor()

        # Get the list of tables in the database
        dbcursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = dbcursor.fetchall()

        records = {}  # Dictionary to store records from each table

        # Iterate through each table and retrieve records by name
        for table in tables:
            table_name = table[0]
            query = f"SELECT * FROM {table_name} WHERE LOWER(Name) = ?"
            dbcursor.execute(query, (name_to_update_lower,))
            records[table_name] = dbcursor.fetchall()

    return records

def delete_record_by_name(name_to_delete, dbcursor):
    # Get the records for the specified name
    records = get_records_by_name(name_to_delete)

    # Display records to the user
    for table_name, record_list in records.items():
        print(f"Records in table '{table_name}' for name '{name_to_delete}':")
        for record in record_list:
            print(record)

    if not any(records.values()):
        print(f"No record found for '{name_to_delete}' in any table.")
        return False

    # Ask for confirmation to delete the record
    confirm_delete = input(f"Do you want to delete the record for '{name_to_delete}'? (yes/no): ").lower()

    if confirm_delete == 'yes':
        # Delete the record(s)
        for table_name, record_list in records.items():
            for record in record_list:
                dbcursor.execute(f"DELETE FROM {table_name} WHERE ID = ?", (record[0],))
                print(f"Record for '{name_to_delete}' deleted successfully from table '{table_name}'.")

        return True
    else:
        print("Deletion canceled.")
        return False

def delete():
    # Example usage: Get the name from the user and delete the corresponding record
    name_to_delete = input("Enter the name to delete: ").strip()

    if not name_to_delete:
        print("Invalid input. Please enter a valid name.")
        return

    # Connect to the SQLite database
    with sql.connect('SQL/sql_project/drivingInstructors.db') as dbconnect:
        dbcursor = dbconnect.cursor()
        record_deleted = delete_record_by_name(name_to_delete, dbcursor)

    if record_deleted:
        print(f"Record for '{name_to_delete}' found and deleted.")
    else:
        print(f"No record found for '{name_to_delete}'.")

if __name__ == "__main__":
    delete()
