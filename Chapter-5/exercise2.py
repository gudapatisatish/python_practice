# Exercise 2: Write another program that prompts for a list of numbers
# as above and at the end prints out both the maximum and minimum of
# the numbers instead of the average.

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

num_lst = list()
while True:
    try:
        inp = input("Enter a number: ")
        if inp == "done":
            break
        num_lst.append(int(inp))
    except:
        print("Invalid input")
        continue
print("Max number:-",max(num_lst), "Min number:-",min(num_lst))