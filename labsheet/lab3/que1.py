filename = "file.txt"
try:
    f = open(filename, "w") 
    f.write("This is the first line.\n")
    f.write("Here is the second line.\n")
    f.write("And this is the third line.\n")
except Exception as e:
    print(f"An error occurred: {e}")

try:
    with open(filename, "r") as f:
        contents = f.read()
        print("File contents:\n")
        print(contents)

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")

