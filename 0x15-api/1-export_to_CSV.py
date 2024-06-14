#!/usr/bin/python3
"""
Accessing a REST API for todo lists of employees and exporting data to CSV.
"""

import requests
import sys
import csv

def fetch_employee_todo_list(employee_id):
    """
    Fetches employee's TODO list and exports data to CSV.

    Args:
    - employee_id (str): ID of the employee

    Outputs:
    - Prints employee's TODO list progress.
    - Creates a CSV file named USER_ID.csv with task data.
    """
    try:
        # Fetch employee data
        employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        response = requests.get(employee_url)
        response.raise_for_status()
        employee_data = response.json()

        # Extract employee details
        user_id = employee_data.get('id')
        username = employee_data.get('username')

        # Fetch TODO list for the employee
        todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        response = requests.get(todo_url)
        response.raise_for_status()
        tasks = response.json()

        # Prepare CSV file
        csv_filename = f"{user_id}.csv"
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])

            # Write each task to CSV
            for task in tasks:
                task_completed_status = 'COMPLETED' if task.get('completed') else 'NOT COMPLETED'
                task_title = task.get('title')
                writer.writerow([user_id, username, task_completed_status, task_title])

        # Print summary of tasks
        done_tasks = [task for task in tasks if task.get('completed')]
        print(f"Employee {username} is done with tasks({len(done_tasks)}/{len(tasks)}):")
        for task in done_tasks:
            print(f"\t{task.get('title')}")

        print(f"CSV file '{csv_filename}' has been created with task details.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)
    except IOError as e:
        print(f"Error writing to CSV file: {e}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_employee_todo_list(employee_id)
