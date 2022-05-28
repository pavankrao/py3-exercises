"""Iterate over dictionaries using for loops
     items()
"""

d = {'x': 10, 'y': 20, 'z': 30}
print("Dict key pairs:")
for key, value in d.items():
     print(f"{key} -> {value}")