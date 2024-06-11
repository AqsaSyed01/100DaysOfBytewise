# Program to find the largest of three numbers

# Get user input
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = input("Enter third number: ")

# Determine the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Display the largest number
print(f"The largest number is: {largest}")
