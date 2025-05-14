def show_menu():
    print("\nTo-Do List")
    print("1. View tasks")
    print("2. Add tasks")
    print("3. Mark task as completed")
    print("4. Delete tasks")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else "✗"
        print(f"{i}. [{status}] {task['title']}")

def add_task(tasks):
    title = input("Enter task description: ")
    tasks.append({"title": title, "done": False})
    print("Task added!")

def mark_done(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Task marked as completed.")
        else:
            print("Please enter a valid number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Removed task: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number 1-5.")

if __name__ == "__main__":
    main()