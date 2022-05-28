"""
 find a list of integers with exactly two occurrences
 of nineteen and at least three occurrences of five.
"""


def count_occurances(nums):
    return nums.count(19) == 2 and nums.count(5) >= 3


# test scenarios

# happy path
nums = [19,19,15,5,3,5,5,2]
print(f"{nums} and result is {count_occurances(nums)}")

# negative path
nums = [19,15,15,5,3,3,5,2]
print(f"{nums} and result is {count_occurances(nums)}")

# one off scenario
nums = [19,19,5,5,5,5,5]
print(f"{nums} and result is {count_occurances(nums)}")