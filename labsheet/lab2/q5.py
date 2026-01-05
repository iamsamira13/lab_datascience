text = input("Enter words : ")

if text.strip() == "":
    print("Please enter correct input value")
else:
    letter_count = 0
    for ch in text:
        if ch != " ":
            letter_count += 1

    if letter_count % 2 == 0:
        words = text.split()
        for w in words:
            print(w[::-1])
    else:
        print("letters are odd")


        