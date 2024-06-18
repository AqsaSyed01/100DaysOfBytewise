def are_anagrams(str1, str2):
    # Removing spaces and converting to lowercase
    cleaned_str1 = ''.join(str1.lower().split())
    cleaned_str2 = ''.join(str2.lower().split())
    
    # Sorting characters in both strings and comparing
    return sorted(cleaned_str1) == sorted(cleaned_str2)

# Taking input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Checking if the input strings are anagrams and print the result
if are_anagrams(string1, string2):
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')
