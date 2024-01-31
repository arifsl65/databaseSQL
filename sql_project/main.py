import search
import insert
import update
import delete

def search_menu():
    while True:
        search.search()
        user_input = input("Do you want to return to the main menu? (y/n): ")
        if user_input.lower() != 'y':
            break

def insert_menu():
    while True:
        insert.insert_data_into_table()
        user_input = input("Do you want to return to the main menu? (y/n): ")
        if user_input.lower() != 'y':
            break

def update_menu():
    while True:
        update.Update_field()
        user_input = input("Do you want to return to the main menu? (y/n): ")
        if user_input.lower() != 'y':
            break

def delete_menu():
    while True:
        delete.delete()
        user_input = input("Do you want to return to the main menu? (y/n): ")
        if user_input.lower() != 'y':
            break

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
