inventory = {"apple": 10, "banana": 5, "milk": 2}

def print_low_stock():
    print("Items low in stock (less than 3):")
    low = False
    for item in inventory:
        if inventory[item] < 3:
            print(item, ":", inventory[item])
            low = True
    if not low:
        print("No items are low in stock.")

while True:
    print("\n1. Add new item")
    print("2. Sell item")
    print("3. Show low stock items")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        name = input("Enter item name to add: ").lower()
        qty = input("Enter quantity: ")

        if not qty.isdigit() or name == "":
            print("Please enter correct input value")
            continue

        qty = int(qty)
        if name in inventory:
            inventory[name] += qty
        else:
            inventory[name] = qty
        print(name, "added/updated. New quantity:", inventory[name])

    elif choice == "2":
        name = input("Enter item name to sell: ").lower()
        qty = input("Enter quantity to sell: ")

        if not qty.isdigit() or name == "":
            print("Please enter correct input value")
            continue

        qty = int(qty)
        if name not in inventory:
            print("Item not found in inventory")
        elif inventory[name] < qty:
            print("Not enough stock to sell")
        else:
            inventory[name] -= qty
            print(qty, "units of", name, "sold. Remaining:", inventory[name])

    elif choice == "3":
        print_low_stock()

    elif choice == "4":
        print("Exiting program")
        break 

    else:
        print("Please enter correct input value")