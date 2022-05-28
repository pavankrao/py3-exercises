"""Generate and print a dictionary 
that contains a number in the form (x, x*x)
1. get number from user -> int
2. create a dict
3. generate dict up to n
"""

# get user input
n=int(input("Input a number: "))

# dict constructor
d = dict()

# format dict
for key in range(1, n+1):
     d[key] = key*key
     
print(f"Generated dict is: {d}")
