# Simple Task Manager Project (OOP)

class Task:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority 

    def display(self):
        print(f"Task: {self.title} | Priority: {self.priority}")


class TaskManager:
    def __init__(self):
        self.tasks = [] #variable list 

    def add_task(self, title, priority):
        task = Task(title, priority) # object creation
        self.tasks.append(task) # push to list

    def show_all_tasks(self):
        print("\n--- ALL TASKS ---")
        for task in self.tasks: # loop 
            task.display()
    
    def find_high_priority(self):
        print("\n--- HIGH PRIORITY TASKS ---")
        for task in self.tasks: # loop
            if task.priority.lower() == "high":
                task.display()
        
# ---------------------------
# FUNCTIONS OUTSIDE CLASS
# ---------------------------

def main():
    manager = TaskManager()

    while True:
        print("\n1. Add Task")
        print("2. Show All Tasks")
        print("3. Show High Priority Tasks")
        print("4. Exit")

        choice = input("Choose: ")
        if choice == "1":
            title = input("Enter task title: ")
            priority = input("Priorirty (High/Medium/Low): ")
            manager.add_task(title, priority)

        elif choice == "2":
            manager.show_all_tasks()

        elif choice == "3":
            manager.find_high_priority()
        
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()



