# Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the
# converted temperature.
#Formula	(0°C × 9/5) + 32 = 32°F

def convert_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius_temp = float(input("Enter temperature in celsius: "))
print("Temperature in Fahrenheit:", convert_to_fahrenheit(celsius_temp))