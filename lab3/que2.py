filename = "file.txt"

try:
    with open(filename) as f:
        nums = [] #list to store numbers
        for line in f:
            try:
                nums.append(float(line.strip()))
            except ValueError:
                pass  
    if nums:
        print("Sum =", sum(nums))
        print("Average =", sum(nums)/len(nums))
    else:
        print("No valid numbers found.")

except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")
