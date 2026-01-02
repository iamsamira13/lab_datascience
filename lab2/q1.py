# Movie Ratings Analyzer

# Input format example:
# Inception-9 Avatar-7 Titanic-8 Joker-9
data = input("Enter movies and ratings in format movie-rating: ")

# Replace spaces with commas so everything becomes comma-separated
data = data.replace(" ", ",")

# Split into parts
pairs = data.split(",")

movies = []
ratings = []

for p in pairs:
    if p != "" and "-" in p:
        parts = p.split("-", 1)
        name = parts[0].strip()       # movie name
        rate = parts[1].strip()       # rating as string
        try:
            ratings.append(float(rate))   # allow decimal ratings
            movies.append(name)
        except ValueError:
            print(f"Invalid rating for '{name}', skipping...")

# Ensure we have valid ratings
if not ratings:
    print("No valid ratings entered.")
else:
    # Calculate average
    avg = sum(ratings) / len(ratings)

    # Highest rated movie
    max_rating = max(ratings)
    max_index = ratings.index(max_rating)
    highest_movie = movies[max_index]

    # Above, below, and equal average lists
    above = []
    below = []
    equal = []

    for i in range(len(movies)):
        if ratings[i] > avg:
            above.append(movies[i])
        elif ratings[i] < avg:
            below.append(movies[i])
        else:
            equal.append(movies[i])

    # Output
    print("\nAverage rating:", avg)
    print("Highest rated movie:", highest_movie)
    print("Movies above average:", above)
    print("Movies below average:", below)
    