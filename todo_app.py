import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    title = input("Enter task name: ")
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
        status = "Done" if task["completed"] else "Pending"
        print(f"{index + 1}. {task['title']} [{status}]")

def complete_task(tasks):
    view_tasks(tasks)
    choice = int(input("Enter task number to mark complete: ")) - 1

    if 0 <= choice < len(tasks):
        tasks[choice]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed")
    else:
        print("Invalid task number")

def delete_task(tasks):
    view_tasks(tasks)
    choice = int(input("Enter task number to delete: ")) - 1

    if 0 <= choice < len(tasks):
        tasks.pop(choice)
        save_tasks(tasks)
        print("Task deleted")
    else:
        print("Invalid task number")

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
