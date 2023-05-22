#!/usr/bin/python3
<<<<<<< HEAD
"""python scripts that uses REST API for a given employee ID, returns information about
their TODO list progress"""
=======
"""Python scripts that uses REST API for a given employee ID, returns
information aboutPython scripts that uses REST API ftheir TODO list progress"""
>>>>>>> a3a8bfad842149c311517abfdfc6694f008b209b

import requests
import sys

if __name__ == "__main__":

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
<<<<<<< HEAD

=======
>>>>>>> a3a8bfad842149c311517abfdfc6694f008b209b
    name = user.json().get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    totalTasks = 0
    completed = 0

    for task in todos.json():
        if task.get('userId') == int(userId):
            totalTasks += 1
<<<<<<< HEAD
            if task.get('completed'):
                completed += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, totalTasks))

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('userId') == int(userId) and task.get('completed')]))
=======

            if task.get('completed'):
                completed += 1

                print('Employee {} is done with tasks({}/{}):'
                      .format(name, completed, totalTasks))

                print('\n'.join(["\t " + task.get('title') for
                      task in todos.json()
                      if task.get('userId') == int(userId) and
                      task.get('completed')]))
>>>>>>> a3a8bfad842149c311517abfdfc6694f008b209b
