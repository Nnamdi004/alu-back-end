#!/usr/bin/python3
"""
Fetches and displays TODO list progress for a given employee ID
using JSONPlaceholder REST API.
"""

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


def display_todo_progress(employee, todos):
    """Display the TODO progress in the specified format."""
    done_tasks = [task for task in todos if task.get("completed") is True]
    print(
        f"Employee {employee.get('name')} is done with tasks"
        f"({len(done_tasks)}/{len(todos)}):"
    )
    for task in done_tasks:
        print(f"\t {task.get('title')}")


def main():
    """Main entry point of the script."""
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
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
    display_todo_progress(employee, todos)


if __name__ == "__main__":
    main()

