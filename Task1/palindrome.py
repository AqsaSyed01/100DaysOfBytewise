# Program to check if a string is a palindrome

# Get user input
user_string = input("Enter a string: ")

# Reverse the string
reversed_string = user_string[::-1]

# Check if the string is a palindrome
if user_string == reversed_string:
    print(f"{user_string} is a palindrome")
else:
    print(f"{user_string} is not a palindrome")
