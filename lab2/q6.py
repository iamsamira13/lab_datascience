graph = {
    "A": {"B", "C"},
    "B": {"A", "D"},
    "C": {"A", "D"},
    "D": {"B", "C"}
}

path = input("Enter path separated by space: ").split()

valid = True

for i in range(len(path) - 1):
    if path[i+1] not in graph[path[i]]:
        valid = False
        break

if valid:
    print("Valid path")
else:
    print("Invalid path")
