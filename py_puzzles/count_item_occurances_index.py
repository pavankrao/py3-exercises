"""
accept a list of integers and
check the length and the fifth element.
Return true if
    the length of the list is 8 and
    fifth element occurs thrice in the said list.
"""

def count_occurance_index(nums):
    return len(nums) == 8 and nums.count(nums[4]) == 3

# Test scenarios

# happy path
nums = [19,19,15,5,5,5,1,2]
print(f"Original list is {nums} and the result is {count_occurance_index(nums)}")

# negative path
nums = [19,15,5,7,5,5,2]
print(f"Original list is {nums} and the result is {count_occurance_index(nums)}")

# one off, len is 8, but 5 count 2
nums = [19,19,15,5,5,4,1,2]
print(f"Original list is {nums} and the result is {count_occurance_index(nums)}")

# one off, len is 7, but 5 count is 3
nums = [19,19,5,5,5,1,2]
print(f"Original list is {nums} and the result is {count_occurance_index(nums)}")