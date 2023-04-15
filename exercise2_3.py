# Exercise 3: Write a program to prompt the user for hours and rate per
# hour to compute gross pay.
# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25

def pay(hours,rate):
    return hours*rate

hours = int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
print("Pay:", pay(hours,rate))