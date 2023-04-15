# Exercise 1: Rewrite your pay computation to give the employee 1.5
# times the hourly rate for hours worked above 40 hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

def pay(hours,rate):
    if hours <= 40:
        return hours*rate
    else:
        return ((40*rate)+((hours-40)*1.5*rate))

h = float(input("Enter Hours: "))
r = float(input("Enter Rate: "))
print("Pay:", pay(h, r))
