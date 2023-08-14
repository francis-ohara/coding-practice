"""Test the Counter class from Python's collections module"""
from collections import Counter

counter = Counter([1, 2, 1, 1, 3, 3, 4, 4, 5, 1, 2, 4, 6])
print(counter)

# find 3 most common elements
print(counter.most_common(3))

# Basically an application of a Python dictionary as a histogram
# Adds some methods for useful things you might want to do in such applications.
