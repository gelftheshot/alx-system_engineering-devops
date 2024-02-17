#!/usr/bin/python3
"""
    Python script to export data in the CSV format.
"""
import json
import requests
import sys
if __name__ == "__main__":
    user_id = int(sys.argv[1])
    employes = requests.get("https://jsonplaceholder.typicode.com/users")
    user_name = [x["username"] for x in employes.json() if x["id"] == user_id]
    if user_name:
        user_name = user_name[0]
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    user_todos = [x for x in todos.json() if x["userId"] == user_id]
    name = str(user_id) + ".json"
    new_todos = [
        {
            "task": data["title"],
            "completed": data["completed"],
            "username": user_name
        }
        for data in user_todos
    ]
    dic = {user_id: new_todos}
    with open(name, "w") as file:
        json.dump(dic, file)
