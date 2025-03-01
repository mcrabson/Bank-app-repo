import os #allow user to interact with the native pyhon operative system
import json #use to store or transporting data
import sys
from datetime import datetime

print("\nWELCOME TO TODO LIST MANAGER ")
class TodoListManager:
    def __init__(self):
        self.user_name: str = input("\nEnter your name to continue: ")
        self.active_tasks = self.load_tasks('Active.txt')
        self.completed_tasks = self.load_tasks('Completed.txt')
        self.deleted_tasks = self.load_tasks('Deleted.txt')
        self.task_id_counter = len(self.active_tasks) + 1
        self.main_menu()

    def load_user_name(self):
        if os.path.exists('names.txt'):
            with open('names.txt', 'r') as file:
                return file.read().strip()
        else:
            name = input("Enter your name: ")
            with open('names.txt', 'w') as file:
                file.write(name)
            return name

    def load_tasks(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self, filename, tasks):
        with open(filename, 'w') as file:
            json.dump(tasks, file)

    def main_menu(self):
        print(f"""\nHello {self.user_name} , this is your Todo List manager. 
        
How may I help you today?""")

        while True:
            print("\nMain Menu:")
            print("1. Add Task")
            print("2. View Active Tasks")
            print("3. View Completed Tasks")
            print("4. View Deleted Tasks")
            print("5. Edit Task Name")
            print("6. Mark Task as Completed")
            print("7. Delete Task")
            print("8. Exit")
            choice = input("Choose an option: ")
            self.handle_choice(choice)

    def handle_choice(self, choice):
        if choice == '1':
            self.add_task()
        elif choice == '2':
            self.view_tasks(self.active_tasks, "Active Tasks")
        elif choice == '3':
            self.view_tasks(self.completed_tasks, "Completed Tasks")
        elif choice == '4':
            self.view_tasks(self.deleted_tasks, "Deleted Tasks")
        elif choice == '5':
            self.edit_task_name()
        elif choice == '6':
            self.mark_task_completed()
        elif choice == '7':
            self.delete_task()
        elif choice == '8':
            self.exit_program()
        else:
            print("Invalid option. Please try know what you are doing.")

    def add_task(self):
        task_name = input("Enter the task name: ")
        task = {
            'id': self.task_id_counter,
            'name': task_name,
            'time_created': datetime.now().isoformat()
        }
        self.active_tasks.append(task)
        self.task_id_counter += 1
        print(f"{self.user_name}, your Task has added successfully.")

    def view_tasks(self, tasks, title):
        print(f"\n{title}:")
        for task in tasks:
            print(f"""
            ID: {task['id']}, 
            Name: {task['name']}, 
            Created: {task['time_created']}"""
                  )
        else:
             print(" = Task list Empty")

    def edit_task_name(self):
        self.view_tasks(self.active_tasks, "Active Tasks")
        task_id = int(input("Enter the task ID to edit: "))
        for task in self.active_tasks:
            if task['id'] == task_id:
                new_name = input("Enter the new task name: ")
                task['name'] = new_name
                print(f"{self.user_name}Task name updated successfully.")
                return
        print("Task ID not found.")

    def mark_task_completed(self):
        self.view_tasks(self.active_tasks, "Active Tasks")
        task_id = int(input("Enter the task ID to mark as completed: "))
        for task in self.active_tasks:
            if task['id'] == task_id:
                task['time_finished'] = datetime.now().isoformat()
                self.completed_tasks.append(task)
                self.active_tasks.remove(task)
                print("Task marked has completed.")
                return
        print("Task ID not found.")

    def delete_task(self):
        self.view_tasks(self.active_tasks, "Active Tasks")
        task_id = int(input("Enter the task ID to delete: "))
        for task in self.active_tasks:
            if task['id'] == task_id:
                self.deleted_tasks.append(task)
                self.active_tasks.remove(task)
                print("Task deleted successfully.")
                return
        print("Task ID not found.")

    def exit_program(self):
        self.save_tasks('Active.txt', self.active_tasks)
        self.save_tasks('Completed.txt', self.completed_tasks)
        self.save_tasks('Deleted.txt', self.deleted_tasks)
        print("\nYou have selected exit program")
        print(f"\nThanks {self.user_name}, All tasks are saved. and your program exit successfully  .")
        print(f"\n So sad to see go {self.user_name}. visit again soon")
        sys.exit()

if __name__ == "__main__":
    TodoListManager()
