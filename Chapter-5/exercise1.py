# Exercise 1: Write a program which repeatedly reads numbers until the
# user enters “done”. Once “done” is entered, print out the total, count,
# and average of the numbers. If the user enters anything other than a
# number, detect their mistake using try and except and print an error
# message and skip to the next number.
# 5.9. EXERCISES 65
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333

total = 0
count = 0
average = 0
while True:
    try:
        i = input("Enter a number: ")
        if i == "done":
            break
        i = int(i)
        count += 1
        total += i
    except:
        print("Invalid input")
        continue
if total == 0:
    average = 0
else:
    average = total/count

print(total, count, average)