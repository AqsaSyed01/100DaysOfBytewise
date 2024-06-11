# Program to print the Fibonacci sequence up to n terms

# Get user input
n_terms = int(input("How many terms? "))

# Initialize the first two terms of the Fibonacci sequence
a, b = 0, 1

# Print the Fibonacci sequence
print("Fibonacci sequence:")
for _ in range(n_terms):
    print(a, end=" ")
    a, b = b, a + b
