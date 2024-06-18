def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

# Take input from the user
n = int(input("Enter the position to find the corresponding Fibonacci number: "))

# Get the nth Fibonacci number
fib_number = fibonacci(n)

# Print the result
if isinstance(fib_number, str):
    print(fib_number)
else:
    print(f"The {n}th Fibonacci number is {fib_number}.")
