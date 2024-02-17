#!/usr/bin/python3
"""
    Python script to export data in the CSV format.
"""
import json
import requests
import sys
if __name__ == "__main__":

    employes = requests.get("https://jsonplaceholder.typicode.com/users")
    dic = {}
    for data in employes.json():
        user_id = data["id"]
        user_name = data["username"]
        todos = requests.get("https://jsonplaceholder.typicode.com/todos")
        user_todos = [x for x in todos.json() if x["userId"] == user_id]
        name = "todo_all_employees.json"
        new_todos = [
            {
                "username": user_name,
                "task": dataa["title"],
                "completed": dataa["completed"]
            }
            for dataa in user_todos
        ]
        dic.update({user_id: new_todos})
    with open(name, "w") as file:
        json.dump(dic, file)
