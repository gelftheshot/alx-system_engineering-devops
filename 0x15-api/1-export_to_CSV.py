#!/usr/bin/python3
"""
    Python script to export data in the CSV format.
"""
import requests
import sys
import csv
if __name__ == "__main__":
    user_id = int(sys.argv[1])
    employes = requests.get("https://jsonplaceholder.typicode.com/users")
    user_name = [x["username"] for x in employes.json() if x["id"] == user_id]
    if user_name:
        user_name = user_name[0]
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    user_todos = [x for x in todos.json() if x["userId"] == user_id]
    name = str(user_id) + ".csv"
    with open(name, "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for data in user_todos:
            row = [data["userId"], user_name, data["completed"], data["title"]]
            writer.writerow(row)
