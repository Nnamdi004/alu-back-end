#!/usr/bin/python3
"""
Exports TODO list information for a given employee ID to a CSV file.
"""

import csv
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


def export_to_csv(employee_id, username, todos):
    """Export TODOs to a CSV file."""
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                str(task.get("completed")),
                task.get("title")
            ])


def main():
    """Main entry point of the script."""
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
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
    export_to_csv(employee_id, employee.get("username"), todos)


if __name__ == "__main__":
    main()
