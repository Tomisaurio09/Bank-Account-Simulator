from task import Task
import json
from datetime import datetime
from validation import validate_input


def add_task(tasks_json):
    task_name = input("Tell me the name of the task: ").capitalize()
    task_description = input("Give me a short description of the task: ").capitalize()
    task_priority = input("Tell me the priority of the task: ").capitalize()
    task_due_date = None

    while not task_due_date:
        deadline = input("Tell me the deadline of the task (DD/MM/YYYY): ")
        try:
            task_due_date = datetime.strptime(deadline, "%d/%m/%Y")
            task_due_date = task_due_date.strftime("%d/%m/%Y")
        except ValueError:
            print("Invalid date. Please, use the format DD/MM/YYYY.")
            print("An example of a valid date would be: 05/09/2006")

    task_object = Task(task_name, task_description,task_due_date,task_priority,False)

    tasks_json[task_object.name] = {
        "description": task_object.description,
        "due_date": task_object.due_date,
        "priority": task_object.priority,
        "state": task_object.status
    }

    return tasks_json
