import search
import insert
import update
import delete

def search_menu():
    search.search_across_tables()

def insert_menu():
    insert.insert_data_into_table()

def update_menu():
    update.Update_field()

def delete_menu():
    delete.delete_instructor()

def exit_menu():
    print("Exiting the program.")
    return True

def main():
    menu_options = {
        '1': search_menu,
        '2': insert_menu,
        '3': update_menu,
        '4': delete_menu,
        '5': exit_menu
    }

    while True:
        print("\nChoose an operation:")
        print("1. Search")
        print("2. Insert")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        selected_menu = menu_options.get(choice, lambda: print("Invalid choice"))
        selected_menu()  # Execute the selected menu option

        if choice == '5':
            print("Exiting the module.")
            break

if __name__ == "__main__":
    main()
