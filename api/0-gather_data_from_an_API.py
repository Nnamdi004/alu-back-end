#!/usr/bin/python3
"""
This script retrieves and displays the TODO list progress of a given employee ID
from the JSONPlaceholder REST API.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    # Fetch employee info
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(user_url)
    if response.status_code != 200:
        print("Employee not found")
        sys.exit(1)

    user = response.json()
    employee_name = user.get("name")

    # Fetch employee's todos
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(todos_url)
    todos = response.json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed") is True]

    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

