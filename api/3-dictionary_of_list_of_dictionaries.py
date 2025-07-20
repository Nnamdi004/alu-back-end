#!/usr/bin/python3
"""
Exports all employees' TODO list information to a JSON file.
"""

import json
import requests


def fetch_all_users():
    """Fetch all users."""
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    if response.status_code != 200:
        return []
    return response.json()


def fetch_user_todos(user_id):
    """Fetch todos for a specific user."""
    url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    response = requests.get(url)
    if response.status_code != 200:
        return []
    return response.json()


def export_all_to_json():
    """Export all employees' TODOs to a JSON file."""
    users = fetch_all_users()
    all_data = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        todos = fetch_user_todos(user_id)

        all_data[str(user_id)] = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos
        ]

    with open("todo_all_employees.json", mode='w') as jsonfile:
        json.dump(all_data, jsonfile)


if __name__ == "__main__":
    export_all_to_json()
