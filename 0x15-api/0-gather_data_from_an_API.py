#!/usr/bin/python3
"""
Accessing a REST API for todo lists of employees.
Usage: python script_name.py <employee_id>
"""

import requests
import sys

def fetch_employee_todo_list(employee_id):
    """
    Fetches and displays the TODO list progress of an employee.

    Args:
    - employee_id (str): ID of the employee
    
    Prints:
    - Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
      TASK_TITLE
      ...
    """
    try:
        # Fetch employee data
        employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        response = requests.get(employee_url)
        response.raise_for_status()
        employee_data = response.json()

        # Extract employee name
        employee_name = employee_data.get('name')

        # Fetch TODO list for the employee
        todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        response = requests.get(todo_url)
        response.raise_for_status()
        tasks = response.json()

        # Calculate number of tasks and completed tasks
        total_tasks = len(tasks)
        completed_tasks = [task for task in tasks if task.get('completed')]
        number_of_done_tasks = len(completed_tasks)

        # Print header
        print(f"Employee {employee_name} is done with tasks"
              "({number_of_done_tasks}/{total_tasks}):")

        # Print completed tasks
        for task in completed_tasks:
            print(f"\t{task.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_employee_todo_list(employee_id)
