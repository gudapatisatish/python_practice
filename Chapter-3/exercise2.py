# Exercise 2: Rewrite your pay program using try and except so that your
# program handles non-numeric input gracefully by printing a message
# and exiting the program. The following shows two executions of the
# program:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input
from sys import exit
def pay(hours, rate):
    if hours>40:
        return ((40*rate)+((hours-40)*1.5*rate))
    else:
        return hours*rate

try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter rate: "))
except:
    print("Error, please enter numeric input")
    exit()

print("Pay:", pay(hours,rate))