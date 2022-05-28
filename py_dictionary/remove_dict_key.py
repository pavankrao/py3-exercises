"""
Remove a key from a dictionary
"""

myDict = {'a':1,'b':2,'c':3,'d':4}
print(myDict)

# remove dict key
if 'a' in myDict:
     #del myDict['a']
     myDict.pop('a')

print(myDict)