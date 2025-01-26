
tasks = []

def show_tasks():
    if tasks:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("\nNo tasks in your list.")

def add_task(task):
    tasks.append(task)
    print(f"Added task: {task}")

def remove_task(task_index):
    if 0 <= task_index < len(tasks):
        removed = tasks.pop(task_index)
        print(f"Removed task: {removed}")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\n--- To-Do List Application ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            show_tasks()
        elif choice == "2":
            task = input("Enter a new task: ")
            add_task(task)
        elif choice == "3":
            show_tasks()
            try:
                task_number = int(input("Enter task number to remove: ")) - 1
                remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
