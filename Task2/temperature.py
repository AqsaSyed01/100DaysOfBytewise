def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def temperature_converter(celsius):
    fahrenheit = celsius_to_fahrenheit(celsius)
    kelvin = celsius_to_kelvin(celsius)
    return f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit and {kelvin} degrees Kelvin."

# Input temperature in Celsius
celsius = int (input("Enter the temperature in celsius"))
# Call the function and print the result
print(temperature_converter(celsius))
