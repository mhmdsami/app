# map
arr = ['me', 'we', 'you', 'i', 'us', 'them']
new_arr = list(map(lambda x: x.title(), arr))

print(new_arr)

# filter
scores = [66, 90, 42, 59, 76, 60, 39, 74, 81, 49]
passed = list(filter(lambda x: x >= 50, scores))

print(passed)

# reduce
from functools import reduce
numbers = [3, 4, 7, 9, 34, 12]
res = reduce(lambda x, y: x + y, numbers)

print(res)

# reduce with initial value
res = reduce(lambda x, y: x + y, numbers, 46)

print(res)
