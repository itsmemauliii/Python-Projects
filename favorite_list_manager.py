# A simple program to manage your favorite list

def display_menu():
    print("\nFavorite List Manager")
    print("1. Add to favorite list")
    print("2. Remove from favorite list")
    print("3. View favorite list")
    print("4. Exit")

def add_to_list(favorite_list):
    item = input("Enter the item to add to your favorite list: ")
    favorite_list.append(item)
    print(f"'{item}' has been added to your favorite list.")

def remove_from_list(favorite_list):
    item = input("Enter the item to remove from your favorite list: ")
    if item in favorite_list:
        favorite_list.remove(item)
        print(f"'{item}' has been removed from your favorite list.")
    else:
        print(f"'{item}' is not in your favorite list.")

def view_list(favorite_list):
    if favorite_list:
        print("\nYour Favorite List:")
        for idx, item in enumerate(favorite_list, start=1):
            print(f"{idx}. {item}")
    else:
        print("\nYour favorite list is empty.")

def main():
    favorite_list = []

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_to_list(favorite_list)
        elif choice == '2':
            remove_from_list(favorite_list)
        elif choice == '3':
            view_list(favorite_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
