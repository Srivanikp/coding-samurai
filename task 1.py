import os
def display_menu():
    print("Todo List Menu:")
    print("1. View tasks")
    print("2. View completed tasks")
    print("3. Add task")
    print("4. Mark task as complete")
    print("5. Delete task")
    print("6. Save tasks")
    print("7. Load tasks")
    print("8. Exit")

def view_tasks(tasks, completed=False):
    if tasks:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            if completed == task.get("completed", False):
                print(f"{i}. {task['description']} {'(Complete)' if task['completed'] else ''}")
    else:
        print("No tasks.")

def add_task(tasks):
    task_description = input("Enter a new task: ")
    tasks.append({"description": task_description, "completed": False})
    print("Task added successfully!")


def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f"Task '{deleted_task['description']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid task number.")

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['description']}|{task['completed']}\n")
    print("Tasks saved successfully!")
def load_tasks():
    tasks = []
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if not line:
                    continue  # Skip empty lines
                try:
                    description, completed_str = line.split('|')
                    tasks.append({"description": description, "completed": completed_str.lower() == 'true'})
                except ValueError:
                    print(f"Skipping invalid line: {line}")
        print("Tasks loaded successfully!")
    else:
        print("No tasks file found. Creating an empty tasks list.")
    return tasks
def main():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            view_tasks(tasks, completed=True)
        elif choice == "3":
            add_task(tasks)
        elif choice == "4":
            mark_task_complete(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            save_tasks(tasks)
        elif choice == "7":
            tasks = load_tasks()
        elif choice == "8":
            print("Exiting the todo list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
