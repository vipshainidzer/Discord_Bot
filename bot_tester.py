import json


with open("users.json", "r") as file:
    data = json.load(file)
    if "630654405045256192" in data:
        print("yes")
        data["630654405045256192"]["experience"] += 10

with open("users.json", "w") as file:
    json.dump(data, file)
