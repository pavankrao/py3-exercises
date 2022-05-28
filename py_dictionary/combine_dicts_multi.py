"""
Merge two Python dictionaries
"""

# Method-1

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)

# Method-2
def merge_dictionaries(*dicts):
     #dicts is local to this function
     result = dict()
     for d in dicts:
          result.update(d)
     return result

students1 = {
  'Theodore': 10,
  'Mathew': 11,
}
students2 = {
  'Roxanne': 9
}

print(f"Original dicts are {students1} and {students2}")
print(f"Combined dicts is {merge_dictionaries(students1, students2)}")