"""
#License: https://bit.ly/3oLErEI
Python program to check a given list of integers 
where the sum of the first i integers is i.
"""


def sum_of_integers(lst):
     return all([sum(lst[:i]) == i for i in range(len(lst))])


# test conditions
# positive
print(f"For [1,1,1,1,1,1,1,1] result in {sum_of_integers([1,1,1,1,1,1,1,1])}")

# negative
print(f"For [2,2,2,2,2,2,2,2] result in {sum_of_integers([2,2,2,2,2,2,2,2])}")