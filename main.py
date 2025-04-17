"""
Functionalities:

Add a new task
Mark Task as Completed
Edit a Task
Delete a Task
View all Task
Filter Tasks
Save and load Tasks (JSON)

"""
from task_manager import *
import json
from validation import validate_input

tasks_file = "data/tasks.json"
try:
    with open(tasks_file, 'r') as file:
        tasks = json.load(file)
except FileNotFoundError:
    print(f"Error: The file '{tasks_file}' is not found.")
    tasks = {}
except json.JSONDecodeError:
    print(f"Error: The file '{tasks_file}' contains invalid JSON data.")
    tasks = {}
except Exception as e:
    print(f"An unexpected error occurred while reading the file: {e}")
    tasks = {}

def introduction():
    print("Hello User!, This is a To-Do-App")
    print("In this app, you can do the next: ")
    print("1- Add Tasks")
    print("2- Mark Task as Completed")
    print("3- Edit a Task")
    print("4- Delete a Task")
    print("5- View all Tasks")
    print("6- Filter Tasks")


#You need to handle the user input and loop later

def main():
    introduction()

    print("\nWhat do you want to do?")
    print("""
        1. Add a Task
        2. Delete a Task
        3. Check the incomplete tasks
        4. Change the task status
        5. Exit the program
            """)
    
    user_choice = validate_input("Choose one of the available options: ", ["1", "2", "3", "4", "5"])

    if user_choice == "1":
        added = add_task(tasks)
        try:
            with open(tasks_file, "w") as file:
                json.dump(added, file, indent=4)
        except Exception as e:
            print(f"An unexpected error occurred while writing to the file: {e}")

main()