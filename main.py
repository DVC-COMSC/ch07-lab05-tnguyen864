# Take 5 values in one string and split values by space
print("Enter 5 integer values as one string:")
strval = input().split()
numbers = []		# List for numbers
for v in strval:
	numbers.append(int(v))		# Convert string to int and append to list

# Get value to count occurrences of
search = int(input("Enter an integer value to search for: "))

# Count number of occurences of number given
found = numbers.count(search)

# Print list and occurences
print("List:", numbers)
print("The occurrences of", search, "=", found)