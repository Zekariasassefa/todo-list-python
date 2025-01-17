# todo_list.py

import os

def show_menu():
    print("\nTo-Do List App")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")
    return choice

def view_tasks(tasks):
    if tasks:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("\nYour To-Do List is empty!")

def add_task(tasks):
    task = input("\nEnter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def remove_task(tasks):
    if not tasks:
        print("\nNo tasks to remove!")
        return
    
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' removed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    
    while True:
        choice = show_menu()

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("\nExiting the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
