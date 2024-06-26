def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Input number
number = int(input("Enter a number "))

# Calculate the factorial
result = factorial(number)

# Print the output
print(f"The factorial of {number} is {result}.")
