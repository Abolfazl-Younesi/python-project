import os
import pickle
import datetime

# Define a class to represent a task
class Task:
    def __init__(self, description, due_date=None, priority=1, completed=False):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = completed
    
    def __repr__(self):
        return f"{self.description} - Due: {self.due_date.strftime('%m/%d/%Y')} - Priority: {self.priority}"


# Define a class to manage the to-do list
class ToDoList:
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.pkl"
        self.load_tasks()
    
    def add_task(self):
        description = input("Enter task description: ")
        due_date_str = input("Enter due date (MM/DD/YYYY) or leave blank: ")
        if due_date_str:
            due_date = datetime.datetime.strptime(due_date_str, "%m/%d/%Y")
        else:
            due_date = None
        priority = int(input("Enter priority (1-5, 5 is highest): "))
        task = Task(description, due_date, priority)
        self.tasks.append(task)
        print("Task added successfully.")
    
    def list_tasks(self):
        print("Tasks:")
        for i, task in enumerate(self.tasks):
            print(f"{i+1}. {task}")
    
    def complete_task(self):
        self.list_tasks()
        choice = int(input("Enter the number of the task to mark as completed: "))
        if 1 <= choice <= len(self.tasks):
            task = self.tasks[choice-1]
            task.completed = True
            print("Task marked as completed.")
        else:
            print("Invalid choice.")
    
    def remove_task(self):
        self.list_tasks()
        choice = int(input("Enter the number of the task to remove: "))
        if 1 <= choice <= len(self.tasks):
            task = self.tasks[choice-1]
            self.tasks.remove(task)
            print("Task removed successfully.")
        else:
            print("Invalid choice.")
    
    def save_tasks(self):
        with open(self.filename, "wb") as f:
            pickle.dump(self.tasks, f)
    
    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "rb") as f:
                self.tasks = pickle.load(f)
    
    def sort_tasks(self):
        self.tasks.sort(key=lambda task: (task.completed, task.priority, task.due_date))
    
    def display_menu(self):
        print("\nTo-Do List Manager\n")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Save Tasks")
        print("6. Exit")
    
    def run(self):
        while True:
            self.sort_tasks()
            self.display_menu()
            choice = input("Enter your choice (1-6): ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.list_tasks()
            elif choice == "3":
                self.complete_task()
            elif choice == "4":
                self.remove_task()
            elif choice == "5":
                self.save_tasks()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")

# Create a to-do list and run the program
todo_list = ToDoList()
todo_list.run()