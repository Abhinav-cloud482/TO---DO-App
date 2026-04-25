import pickle
import os

TASKS_FILE = 'tasks.pkl'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'rb') as f:
            return pickle.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'wb') as f:
        pickle.dump(tasks, f)

def add_task(title, tasks):
    task = {"title": title, "done": False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {title}")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Your tasks:")
        for idx, task in enumerate(tasks, 1):
            status = "[x]" if task["done"] else "[ ]"
            print(f"{idx}. {status} {task['title']}")

def delete_task(index, tasks):
    try:
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Task removed: {removed['title']}")
    except IndexError:
        print("Invalid task number.")

def mark_task_completed(index, tasks):
    try:
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print(f"Task marked as completed: {tasks[index - 1]['title']}")
    except IndexError:
        print("Invalid task number.")

def menu():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Mark task as completed")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            view_tasks(tasks)

        elif choice == '2':
            title = input("Enter new task: ").strip()
            if title:
                add_task(title, tasks)
            else:
                print("Task cannot be empty.")

        elif choice == '3':
            view_tasks(tasks)
            try:
                index = int(input("Enter task number to delete: "))
                delete_task(index, tasks)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            view_tasks(tasks)
            try:
                index = int(input("Enter task number to mark as completed: "))
                mark_task_completed(index, tasks)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    menu()
