def longest_palindromic_substring(s):
    # Helper function to expand around center and find palindrome
    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    if not s:
        return ""

    longest = ""
    for i in range(len(s)):
        # Odd-length palindromes
        substring1 = expand_around_center(s, i, i)
        # Even-length palindromes
        substring2 = expand_around_center(s, i, i + 1)
        # Update longest palindrome found
        if len(substring1) > len(longest):
            longest = substring1
        if len(substring2) > len(longest):
            longest = substring2

    return longest

# Get input string from the user
input_string = input("Enter a string: ")

# Find and print the longest palindromic substring
result = longest_palindromic_substring(input_string)
print(f"Longest palindromic substring in '{input_string}' is '{result}'")
