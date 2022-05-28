"""Write a Python script to print a dictionary 
1. where the keys are numbers between 1 and 15 (both included) and 
2. the values are square of keys - use of x**2
"""

d = dict()

for key in range(1,16):
     d[key] = key**2

print(f"Result is: {d}")