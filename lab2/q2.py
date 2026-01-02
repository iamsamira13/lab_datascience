# Unique Words Collector

import string

# Take paragraph input
paragraph = input("Enter a paragraph: ")

# Split into words
words = paragraph.split()

# Normalize: lowercase + strip punctuation
unique_words = []
for w in words:
    w = w.lower().strip(string.punctuation)
    if w and w not in unique_words:   # avoid empty strings
        unique_words.append(w)

# Sort alphabetically
unique_words.sort()

# Output
print("\nUnique words (alphabetical):")
print(", ".join(unique_words))
print("Total unique words:", len(unique_words))
