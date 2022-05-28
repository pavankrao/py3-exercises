"""Check whether a given key already exists in a dictionary"""

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def is_key_present(key):
     if key in d:
          print("key is present")
     else:
          print("key is not present")

is_key_present(1)
is_key_present(9)
