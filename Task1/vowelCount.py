# Program to count the number of vowels in a string

# Get user input
user_string = input("Enter a string: ")

# Define a set of vowels
vowels = set('aeiouAEIOU')

# Count the number of vowels in the string
vowel_count = sum(1 for char in user_string if char in vowels)

# Display the number of vowels
print(f"The number of vowels is: {vowel_count}")
