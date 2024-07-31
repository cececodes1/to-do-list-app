tasks = []  # Initialize an empty list to store tasks

def display_menu():
    #Display the menu for the To-Do List App
    print("Welcome to the To-Do List App!")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def get_user_input():
    while True:
        try:
            user_input = int(input("Choose an option (1, 2, 3, 4, 5): "))
            if 1 <= user_input <= 5:
                return user_input
            else:
                print("Invalid option. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def add_task():
    #Add a new task to the list
    task_name = input("Enter the task name: ")
    task = {"name": task_name, "status": "Incomplete"}
    tasks.append(task)
    print(f"Task '{task_name}' added successfully!")

def view_tasks():
    #Display the list of tasks
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "X" if task["status"] == "Complete" else " "
            print(f"{i}. {task['name']} [{status}]")

def mark_task_complete():
    #Mark a task as complete
    if not tasks:
        print("No tasks available.")
    else:
        view_tasks()
        task_number = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_number <= len(tasks):
            task = tasks[task_number - 1]
            task["status"] = "Complete"
            print(f"Task '{task['name']}' marked as complete!")
        else:
            print("Invalid task number.")

def delete_task():
    #Delete a task
    if not tasks:
        print("No tasks available.")
    else:
        view_tasks()
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            task = tasks.pop(task_number - 1)
            print(f"Task '{task['title']}' deleted successfully!")
        else:
            print("Invalid task number.")

def main():
    while True:
        display_menu()
        user_choice = get_user_input()
        if user_choice == 1:
            add_task()
        elif user_choice == 2:
            view_tasks()
        elif user_choice == 3:
            mark_task_complete()
        elif user_choice == 4:
            delete_task()
        elif user_choice == 5:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()