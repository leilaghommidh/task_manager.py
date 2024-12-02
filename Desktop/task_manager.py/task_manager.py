import json
from pathlib import Path

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if Path(self.filename).is_file():
            with open(self.filename, "r") as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []


    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file)

    def add_task(self, description):
        task = {"description": description, "completed": False}
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            self.save_tasks()

    def list_tasks(self):
        return self.tasks


if __name__ == "__main__":
    manager = TaskManager()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Complete Task")
        print("4. List Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter task description: ")
            manager.add_task(description)
        elif choice == "2":
            index = int(input("Enter task index to remove: "))
            manager.remove_task(index)
        elif choice == "3":
            index = int(input("Enter task index to complete: "))
            manager.complete_task(index)
        elif choice == "4":
            tasks = manager.list_tasks()
            for i, task in enumerate(tasks):
                status = "✔" if task["completed"] else "✖"
                print(f"{i}: {task['description']} [{status}]")
        elif choice == "5":
            break
        else:
            print("Invalid option. Try again.")
