#Student Marks Manager

def get_grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

students = {}

# Input student data
while True:
    name = input("Enter student name (type 'done' to finish): ")
    if name.lower() == "done":
        break

    marks_input = input("Enter marks for 3 subjects of (separated by , or -): ")

    # Replace '-' with ',' so both separators work
    marks_input = marks_input.replace("-", ",")

    # Split into list and convert to integers
    marks = []
    for m in marks_input.split(","):
        if m.strip().isdigit():
            marks.append(int(m.strip()))

    students[name] = marks

print("\nStudent Results:")

averages = {}

# Calculate average and grade
for name in students:
    total = 0
    for m in students[name]:
        total = total + m

    avg = total / len(students[name])   # flexible, not hardcoded
    averages[name] = avg
    grade = get_grade(avg)

    print(name, "Average:", round(avg, 2), "Grade:", grade)

# Find top 2 students (simple sort)
names = list(averages.keys())
for i in range(len(names)):
    for j in range(i + 1, len(names)):
        if averages[names[j]] > averages[names[i]]:
            names[i], names[j] = names[j], names[i]

print("\nTop 2 Students:")
print(names[0], "- Average:", round(averages[names[0]], 2), "Grade:", get_grade(averages[names[0]]))
if len(names) > 1:
    print(names[1], "- Average:", round(averages[names[1]], 2), "Grade:", get_grade(averages[names[1]]))
