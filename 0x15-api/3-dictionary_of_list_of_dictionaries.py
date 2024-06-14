#!/usr/bin/python3
"""
Accessing a REST API for todo lists of employees and exporting data to JSON.
"""

import requests
import sys
import json

def fetch_all_employees_todo_lists():
    """
    Fetches TODO lists for all employees and exports data to a single JSON file.

    Outputs:
    - Creates a JSON file named todo_all_employees.json with task data for all employees.
    """
    try:
        # Fetch all employees
        users_url = "https://jsonplaceholder.typicode.com/users"
        response = requests.get(users_url)
        response.raise_for_status()
        employees = response.json()

        # Prepare data structure for all employees' TODO lists
        todo_data = {}
        
        for employee in employees:
            employee_id = employee['id']
            username = employee['username']
            todo_data[employee_id] = []
            
            # Fetch TODO list for the employee
            todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
            response = requests.get(todo_url)
            response.raise_for_status()
            tasks = response.json()
            
            # Collect tasks data for the employee
            for task in tasks:
                task_info = {
                    "username": username,
                    "task": task.get('title'),
                    "completed": task.get('completed')
                }
                todo_data[employee_id].append(task_info)

        # Write JSON data to file
        json_filename = "todo_all_employees.json"
        with open(json_filename, 'w') as json_file:
            json.dump(todo_data, json_file, indent=4)

        print(f"JSON file '{json_filename}' has been created with task details for all employees.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)
    except IOError as e:
        print(f"Error writing to JSON file: {e}")
        sys.exit(1)

if __name__ == '__main__':
    fetch_all_employees_todo_lists()
