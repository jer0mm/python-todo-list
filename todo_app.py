import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                data = json.load(file)
                return data if isinstance(data, list) else []
        except (json.JSONDecodeError, IOError):
            print("Error reading task file. Starting with empty list.")
    return []


def save_tasks(tasks):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(tasks, file, indent=4)
    except IOError:
        print("Error saving tasks.")


def add_task(tasks):
    title = input("Enter task name: ").strip()

    if not title:
        print("Task name cannot be empty")
        return

    task = {
        "title": title,
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available")
        return

    for index, task in enumerate(tasks):
        status = "Done" if task.get("completed") else "Pending"
        print(f"{index + 1}. {task.get('title', 'Unknown Task')} [{status}]")


def complete_task(tasks):
    if not tasks:
        print("No tasks to complete")
        return

    view_tasks(tasks)

    try:
        choice = int(input("Enter task number to mark complete: ")) - 1
        if 0 <= choice < len(tasks):
            tasks[choice]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")


def delete_task(tasks):
    if not tasks:
        print("No tasks to delete")
        return

    view_tasks(tasks)

    try:
        choice = int(input("Enter task number to delete: ")) - 1
        if 0 <= choice < len(tasks):
            tasks.pop(choice)
            save_tasks(tasks)
            print("Task deleted")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")


def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
