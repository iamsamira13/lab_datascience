import json

student = [
    {"id": 1, "name": "Divya", "marks": 50},
    {"id": 2, "name": "Aarav", "marks": 90},
]

# Write JSON
try:
    with open("student.json", "w") as file:
        json.dump(student, file) 
        print("JSON data written successfully")
except Exception as e:
    print("Write error:", e)

# Read JSON
try:
    with open("student.json", "r") as file:
        data = json.load(file)
        print("\nStudent Details:")
        for s in data:   # iterate through the list
            print(f"ID: {s['id']} Name: {s['name']} Marks: {s['marks']}")
except FileNotFoundError:
    print("JSON file not found")
except json.JSONDecodeError:
    print("Invalid JSON format")

