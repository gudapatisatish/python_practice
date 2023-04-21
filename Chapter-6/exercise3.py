# rcise 3: Encapsulate this code in a function named count,
# and generalize it so that it accepts the string and the letter as arguments.

def count_sub_string(string, letter):
    count = 0
    for char in string:
        if char == letter:
            count+=1
    return count

string = input("Enter string: ")
char = input("Enter char: ")
times = count_sub_string(string, char)
print(string,char,times)