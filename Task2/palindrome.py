# Function to check if a word is a palindrome
def is_palindrome(word):
    # Convert the word to lowercase for case-insensitive comparison
    word = word.lower()
    # Check if the word reads the same forwards and backwards
    return word == word[::-1]

# Take input from the user
user_input = input("Enter a word to check if it's a palindrome: ")

# Check if the input word is a palindrome and print the result
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")

