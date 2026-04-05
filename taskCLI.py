import sys
import json 
import os
from datetime import datetime

TASKS_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    tasks = load_tasks()

    new_id = max([t['id'] for t in tasks], default=0)+1

    
    new_task={
        "id": new_id,
        "description": description,
        "status":"todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt":datetime.now().isoformat(),

        }
    
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task addded successfully (ID: {new_id})")


def list_tasks(status_filter=None):
    tasks = load_tasks()
    for task in tasks:
        if status_filter and task['status'] != status_filter:
            continue
        print(f"[{task['id']}] {task['description']} - {task['status']}")


if __name__ == "__main__":
    # sys.argv[0] is the filename, sys.argv[1] is the command (add, list, etc)
    command = sys.argv[1] if len(sys.argv) > 1 else None

    if command == "add":
        description = sys.argv[2]
        add_task(description)
    elif command == "list":
        # Check if the user added a filter like 'done'
        status = sys.argv[2] if len(sys.argv) > 2 else None
        list_tasks(status)
    else:
        print("Usage: python task_cli.py [add/list] [arguments]")
