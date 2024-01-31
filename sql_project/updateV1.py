import sqlite3 as sql

def display_tables():
    print("Choose a table to update:")
    print("1. Table B")
    print("2. Table BA")
    print("0. Exit")

def display_fields():
    print("Choose a field to update:")
    print("1. Name")
    print("2. Email")
    print("3. Phone Number")
    print("4. Distance")
    print("5. Postcode")
    print("0. Exit")

def update_record(cursor, field, new_value, instructor_id, table_name):
    cursor.execute(f"UPDATE {table_name} SET {field} = ? WHERE ID = ?", (new_value, instructor_id))

def Update_field():
    dbconnect = sql.connect('SQL/sql_project/drivingInstructors.db')
    dbcursor = dbconnect.cursor()

    display_tables()
    table_choice = int(input("Enter the number corresponding to the table you want to update: "))

    if table_choice == 0:
        print("Exiting...")
    else:
        table_mappings = {1: "B", 2: "BA"}
        selected_table = table_mappings.get(table_choice)
        if selected_table:
            instructor_id = int(input(f"Enter the ID of the instructor you want to update in {selected_table}: "))
            display_fields()
            field_choice = int(input("Enter the number corresponding to the field you want to update: "))

            if field_choice == 0:
                print("Exiting...")
            else:
                field_mappings = {1: "Name", 2: "Email", 3: "Phone_Number", 4: "Distance", 5: "Postcode"}
                selected_field = field_mappings.get(field_choice)
                if selected_field:
                    new_value = input(f"Enter the new value for {selected_field}: ")
                    update_record(dbcursor, selected_field, new_value, instructor_id, selected_table)
                    dbconnect.commit()
                    print("Record updated successfully!")
                else:
                    print("Invalid choice. Please enter a valid field number.")
        else:
            print("Invalid choice. Please enter a valid table number.")

    dbconnect.close()

if __name__ == "__main__":
    Update_field()
