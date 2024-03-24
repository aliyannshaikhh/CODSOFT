# Define an empty list to store tasks
task_list = []

# Creating a function to display the menu
def display_task_menu():
    print("To-Do List Menu")
    print("1. View Current Tasks")
    print("2. Add a New Task")
    print("3. Delete a Task")
    print("4. Update an Existing Task")
    print("5. Exit")

# Now creating a function to view all the existing tasks
def view_all_tasks():
    if not task_list:
        print("No tasks found. Add some tasks to get started.")
    else:
        print("Tasks:")
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")

# Creating a function to add a new task
def add_new_task():
    new_task = input("Enter your task: ")
    task_list.append(new_task)
    print("Task has been added successfully.")

# Creating a function to delete or remove a task
def remove_task():
    view_all_tasks()
    if task_list:
        try:
            index = int(input("Enter the task's number to delete: ")) - 1
            if 0 <= index < len(task_list):
                deleted_task = task_list.pop(index)
                print(f"'{deleted_task}' was deleted successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input.")
    else:
        print("There are no tasks to delete.")

# Lastly, creating a function to update a task
def update_task():
    view_all_tasks()
    if task_list:
        try:
            index = int(input("Enter the task's number to update: ")) - 1
            if 0 <= index < len(task_list):
                new_task = input("Enter the new task: ")
                task_list[index] = new_task
                print("Task was updated successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input.")
    else:
        print("No tasks to update.")

# Creaating a Main function to run the to-do list application
def run_application():
    while True:
        display_task_menu()
        choice = input("Enter your choice number: ")

        if choice == '1':
            view_all_tasks()
        elif choice == '2':
            add_new_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            update_task()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Kindly, enter a number between 1 and 5.")

if __name__ == "__main__":
    run_application()