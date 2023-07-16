"""Test the possibility of starting an infinite loop through recursion."""

def function(n):
    return function(n)


print(function(1))

# Conclusion Python internally guards against this by throwing an exception called RecursionError whose message is
# "maximum recursion depth exceeded".
