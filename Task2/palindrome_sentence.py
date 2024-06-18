import string

def is_palindrome_sentence(sentence):
    # Remove punctuation and spaces, and convert to lowercase
    cleaned_sentence = ''.join(char.lower() for char in sentence if char.isalnum())
    # Check if the cleaned sentence reads the same forwards and backwards
    return cleaned_sentence == cleaned_sentence[::-1]

# Take input from the user
sentence = input("Enter a sentence to check if it's a palindrome: ")

# Check if the input sentence is a palindrome and print the result
if is_palindrome_sentence(sentence):
    print(f'"{sentence}" is a palindrome.')
else:
    print(f'"{sentence}" is not a palindrome.')
