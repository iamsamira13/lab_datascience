import csv

filename = "student.csv"

try:
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            roll, name, marks = row
            print(f"{roll} | {name} | {marks}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
