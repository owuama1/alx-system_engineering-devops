#!/usr/bin/python3
"""
Python script to fetch and display employee's TODO list progress
using a REST API.
"""

import sys
import requests

# Constants
BASE_URL = 'https://jsonplaceholder.typicode.com'
EMPLOYEE_ENDPOINT = '/users/{}/todos'


def fetch_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress of an employee.

    Args:
    - employee_id (int): ID of the employee

    Prints:
    - Employee EMPLOYEE_NAME is done
      with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
      TASK_TITLE
      ...
    """
    # Construct the URL
    url = BASE_URL + EMPLOYEE_ENDPOINT.format(employee_id)

    try:
        # Fetch data from the API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse JSON response
        todos = response.json()

        # Calculate stats
        total_tasks = len(todos)
        done_tasks = sum(1 for todo in todos if todo['completed'])

        # Get employee name
        employee_name = todos[0]['userId']

        # Print header
        print(f"Employee {employee_name}"
              "is done with tasks({done_tasks}/{total_tasks}):")

        # Print completed tasks
        for todo in todos:
            if todo['completed']:
                print(f"\t{todo['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_employee_todo_progress(employee_id)
