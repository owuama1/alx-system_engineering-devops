#!/usr/bin/python3
"""
Accessing a REST API for todo lists of employees and exporting data to JSON.
"""

import json
import requests
import sys


def fetch_employee_todo_list(employee_id):
    """
    Fetches employee's TODO list and exports data to JSON.

    Args:
    - employee_id (str): ID of the employee

    Outputs:
    - Prints employee's TODO list progress.
    - Creates a JSON file named USER_ID.json with task data.
    """
    try:
        # Fetch employee data
        employee_url = (
            f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        )
        response = requests.get(employee_url)
        response.raise_for_status()
        employee_data = response.json()

        # Extract employee details
        user_id = employee_data.get('id')
        username = employee_data.get('username')

        # Fetch TODO list for the employee
        todo_url = (
            f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        )
        response = requests.get(todo_url)
        response.raise_for_status()
        tasks = response.json()

        # Prepare JSON data
        todo_data = {user_id: []}
        for task in tasks:
            task_info = {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            }
            todo_data[user_id].append(task_info)

        # Write JSON data to file
        json_filename = f"{user_id}.json"
        with open(json_filename, 'w') as json_file:
            json.dump(todo_data, json_file, indent=4)

        # Print summary of tasks
        done_tasks = [task for task in tasks if task.get('completed')]
        print(f"Employee {username} is done with tasks({len(done_tasks)}/"
              f"{len(tasks)}):")
        for task in done_tasks:
            print(f"\t{task.get('title')}")

        print(f"JSON file '{json_filename}'"
              f"has been created with task details.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)
    except IOError as e:
        print(f"Error writing to JSON file: {e}")
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_employee_todo_list(employee_id)
