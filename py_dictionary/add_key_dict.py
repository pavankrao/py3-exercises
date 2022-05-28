"""Add a key to a dictionary"""

d = {0:10, 1:20}
print(d)

# method-1 - adding multiple values
d.update({2:30, 5:50})
print(d)

# method-2 - adding one pair at a time
d[4] = 40
print(d)