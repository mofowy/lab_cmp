import json
import csv

def save_to_json(data, filename="lab7/output.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def save_to_csv(data, filename="lab7/output.csv"):
    with open(filename, "w") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)