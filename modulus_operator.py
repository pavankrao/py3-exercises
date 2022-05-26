"""
#License: https://bit.ly/3oLErEI

accept an integer mod_and_power whether an integer greater than 4^4 and
which is 4 mod 34.

Exponent operation: 4^4 (4**4)
The ** operator in Python is used to raise
the number on the left to the power of the exponent of the right

Modulus operation:
modulo operation returns the remainder or
signed remainder of a division

>>>> If you don't specify function return, then None is returned
"""

def mod_and_power(n):
    return n > 4 ** 4 and n % 34 == 4


# mod_and_power conditions
print("Check whether the said integer greater than 4^4 and which is 7 mod 134 :")

# happy path
n = 922
print(f"Original number is {n} and result is {mod_and_power(n)}")

# negative path
n = 914
print(f"Original number is {n} and result is {mod_and_power(n)}")
