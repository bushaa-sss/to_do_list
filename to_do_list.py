#!/usr/bin/env python3

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def remove_task(self, task_index):
        try:
            task = self.tasks.pop(task_index)
            print(f"Task '{task}' removed successfully.")
        except IndexError:
            print("Invalid task index.")

    def display_tasks(self):
        if self.tasks:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("No tasks.")

    def update_task(self, task_index, new_task):
        try:
            self.tasks[task_index] = new_task
            print("Task updated successfully.")
        except IndexError:
            print("Invalid task index.")

def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add Task\n2. Remove Task\n3. Display Tasks\n4. Update Task\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task_index = int(input("Enter task index to remove: "))
            todo_list.remove_task(task_index - 1)
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            task_index = int(input("Enter task index to update: "))
            new_task = input("Enter new task: ")
            todo_list.update_task(task_index - 1, new_task)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
