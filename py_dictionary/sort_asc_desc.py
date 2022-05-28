"""Python program to sort (ascending and descending) a dictionary by value.
"""

import operator

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(f'Original dictionary : {d}')

# Asc sort by key
asc_sort_key = sorted(d.items(), key=operator.itemgetter(0))
print(f"Asc sort by key {asc_sort_key}")

# Asc sort by value
asc_sort_val = sorted(d.items(), key = operator.itemgetter(1))
print(f"Asc sort by value {asc_sort_val}")

# Desc sort by key
desc_sort_key = sorted(d.items(), key = operator.itemgetter(0), reverse=True)
print(f"Desc sort by key {desc_sort_key}")

# Desc sort by value
desc_sort_val = sorted(d.items(), key = operator.itemgetter(1), reverse=True)
print(f"Desc sort by value {desc_sort_val}")