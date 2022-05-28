"""Concatenate multiple dictionaries 
     to create a new one
     update() is used for combining multiple dicts
"""

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
print(f"Initial dic4 is {dic4}")

for d in (dic1, dic2, dic3):
     dic4.update(d)
     
print(f"Updated dict is {dic4}")