#!/usr/bin/python3
"""
    for a given employee ID, returns information
    about his/her TODO list progress.
"""
import requests
import sys
if __name__ == "__main__":
    user_id = int(sys.argv[1])
    employes = requests.get("https://jsonplaceholder.typicode.com/users")
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    user_todos = [x for x in todos.json() if x["userId"] == user_id]
    name = [x["name"] for x in employes.json() if x["id"] == user_id]
    if name:
        name = name[0]
    ttask = len(user_todos)
    ctask = len([x for x in user_todos if x["completed"] is True])
    print("Employee {} is done with tasks({}/{}):".format(name, ctask, ttask))
    for x in user_todos:
        if x["completed"] is True:
            print("\t {}".format(x["title"]))
