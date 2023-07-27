"""Code for demonstrating the relationship between a for-loop and a list comprehension."""

# list comprehension
input_iterable = range(10)
numbers = [i ** 2 for i in input_iterable]  # generate 1st ten perfect squares
print(numbers)

# for-loop equivalent
input_iterable = range(10)
numbers = []
for i in input_iterable:
    number = i ** 2
    numbers.append(number)
print(numbers)

# conclusion
# My intuition on the relationship between a for-loop and a list comprehension:
# A for loop is a python structure for running a specific block of code for a repeated number of times.
#       - This block of code can be used to do anything.
#       - One of the things you can do with this block of code is to generate an iterable of values.
# A list comprehension is a python syntax used specifically for generating an iterable of values.
#       - List comprehensions therefore perform one subset of the duties performed by a for loop
#         i.e. the generation of iterables.
#       - They were probably created because someone realized that a large proportion of what we do with
#         for-loops is the generation of iterables, so it would be useful to have a simpler, more efficient
#         syntax for doing so.
