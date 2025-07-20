#!/usr/bin/python3
"""
Exports TODO list information for a given employee ID to a JSON file.
"""

import json
import requests
import sys


def fetch_employee_data(employee_id):
    """Fetch employee information by ID."""
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()


def fetch_employee_todos(employee_id):
    """Fetch todos for the given employee ID."""
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    if response.status_code != 200:
        return []
    return response.json()


def export_to_json(employee_id, username, todos):
    """Export TODOs to a JSON file."""
    tasks_list = []
    for task in todos:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        tasks_list.append(task_dict)

    data = {str(employee_id): tasks_list}

    filename = f"{employee_id}.json"
    with open(filename, mode='w') as jsonfile:
        json.dump(data, jsonfile)


def main():
    """Main entry point of the script."""
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    employee = fetch_employee_data(employee_id)
    if not employee:
        print("Employee not found")
        sys.exit(1)

    todos = fetch_employee_todos(employee_id)
    export_to_json(employee_id, employee.get("username"), todos)


if __name__ == "__main__":
    main()
