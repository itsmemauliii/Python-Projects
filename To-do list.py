tasks = []

# Function to display the menu
def display_menu():
    print("\n--- To-Do List App ---")
    print("1. View Tasks")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Clear All Tasks")
    print("5. Exit")

# Function to view tasks
def view_tasks():
    if not tasks:
        print("\nYour task list is empty.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to add a task
def add_task():
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added successfully.")
    else:
        print("Task cannot be empty!")

# Function to remove a task
def remove_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' removed successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Function to clear all tasks
def clear_tasks():
    global tasks
    confirm = input("Are you sure you want to clear all tasks? (yes/no): ").lower()
    if confirm == "yes":
        tasks = []
        print("All tasks cleared.")
    else:
        print("Clear action cancelled.")

# Main application loop
def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            clear_tasks()
        elif choice == "5":
            print("Exiting To-Do List App. Have a productive day!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

# Run the app
if __name__ == "__main__":
    main()
