# Exercise 1: Write a function called chop that takes a list and modifies
# it, removing the first and last elements, and returns None. Then write
# a function called middle that takes a list and returns a new list that
# contains all but the first and last elements.

def chop(lst):
    lst[:] = lst[1:-1]

def middle(lst):
    return lst[1:-1]

lst = [1,2,3,4,5]
new_lst = chop(lst)
print("chop_return", new_lst)
print("lst",lst)

lst = [1,2,3,4,5]
new_lst = middle(lst)
print("middle_return", new_lst)
print("lst", lst)
