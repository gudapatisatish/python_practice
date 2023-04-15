# Exercise 3: Write a program to prompt for a score between 0.0 and
# 1.0. If the score is out of range, print an error message. If the score is
# between 0.0 and 1.0, print a grade using the following table:
# 3.11. EXERCISES 41
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# Enter score: 0.95
# A
# Enter score: perfect
# Bad score
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C
# Enter score: 0.5
# F
# Run the program repeatedly as shown above to test the various different values for
# input.

def grade(score):
    if score>1 or score<0:
        return "Bad score"
    elif score>=0.9:
        return "A"
    elif score>=0.8:
        return "B"
    elif score>=0.7:
        return "C"
    elif score>=0.6:
        return "D"
    else:
        return "F"

try:
    score = float(input("Enter score: "))
except:
    score = -1

print(grade(score))
