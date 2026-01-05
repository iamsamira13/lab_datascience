def write_file(filename):
    try:
        data = input("Enter text to write: ")
        with open(filename, "w") as f:
            f.write(data + "\n")
        print("Data written successfully.")
    except Exception as e:
        print("Write error:", e)


def read_file(filename):
    try:
        with open(filename, "r") as f:
            print("\nFile contents:\n")
            print(f.read())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print("Read error:", e)


def append_file(filename):
    try:
        data = input("Enter text to append: ")
        with open(filename, "a") as f:
            f.write(data + "\n")
        print("Data appended successfully.")
    except Exception as e:
        print("Append error:", e)


def menu():
    filename = "menu_file.txt"
    while True:
        print("\n--- Menu ---")
        print("1. Write to file")
        print("2. Read from file")
        print("3. Append to file")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                write_file(filename)
            elif choice == 2:
                read_file(filename)
            elif choice == 3:
                append_file(filename)
            elif choice == 4:
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1-4.")
        except ValueError:
            print("Invalid input. Please enter a number (1-4).")


# Run the menu
menu()
