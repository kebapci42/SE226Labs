file = open("1000wordsPython.txt", "r")
file.readline() # Pass the first line

words = file.readline().split(",")
print("\nThe words start with letter 'e':")
count = 0

for word in words:
    word = word.strip("\"")
    if word.startswith("e"):
        count = count + 1
        print(str(count) + ") " + word)


print("\nThe words start with letters 'ha':")
count = 0

for word in words:
    word = word.strip("\"")
    if word.startswith("ha"):
        count = count + 1
        print(str(count) + ") " + word)
        
num_of_stars = input("\nPlease, enter an integer between 3 and 9 (inclusive):")
num_of_stars = int(num_of_stars)
upper_bond = 2 * num_of_stars

for i in range(1, upper_bond):
    if i <= num_of_stars:
        print("*" * i)
    else:
        print("*" * (upper_bond - i))