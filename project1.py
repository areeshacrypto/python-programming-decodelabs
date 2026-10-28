import json
import os

TASKS_FILE = "tasks.json"

def load_tasks() -> list:
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []

def save_tasks(tasks: list) -> None:
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks: list, title: str) -> dict:
    task_id = len(tasks) + 1
    new_task = {
        "id": task_id,
        "task": title,
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return new_task

def complete_task(tasks: list, task_index: int) -> bool:
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_tasks(tasks)
        return True
    return False

def delete_task(tasks: list, task_index: int) -> bool:
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        for idx, task in enumerate(tasks, start=1):
            task["id"] = idx
        save_tasks(tasks)
        return True
    return False

def display_menu():
    print("\n      DECODELABS TO-DO LIST ENGINE      ")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit Engine")

def view_tasks(tasks: list):
    if not tasks:
        print("\n[INFO] Your task list is currently empty.")
        return

    print("\nCURRENT TASK QUEUE:")
    for index, task_data in enumerate(tasks, start=1):
        status = "✓" if task_data.get("completed", False) else " "
        print(f"[{index}] [{status}] {task_data['task']}")

def main():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            title = input("\nEnter task title: ").strip()
            if title:
                added = add_task(tasks, title)
                print(f"[SUCCESS] Added task: '{added['task']}'")
            else:
                print("[ERROR] Task title cannot be empty.")

        elif choice == "3":
            view_tasks(tasks)
            if tasks:
                try:
                    num = int(input("\nEnter task number to mark complete: "))
                    if complete_task(tasks, num - 1):
                        print(f"[SUCCESS] Task #{num} marked as complete.")
                    else:
                        print("[ERROR] Invalid task number.")
                except ValueError:
                    print("[ERROR] Please enter a valid number.")

        elif choice == "4":
            view_tasks(tasks)
            if tasks:
                try:
                    num = int(input("\nEnter task number to delete: "))
                    if delete_task(tasks, num - 1):
                        print(f"[SUCCESS] Task #{num} removed.")
                    else:
                        print("[ERROR] Invalid task number.")
                except ValueError:
                    print("[ERROR] Please enter a valid number.")

        elif choice == "5":
            print("\nShutting down backend engine. Data saved to disk.")
            break

        else:
            print("[ERROR] Invalid option. Please enter 1-5.")

if __name__ == "__main__":
    main()