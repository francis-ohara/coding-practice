"""Test how to use the Python assert statement."""


# define function for adding numbers
def add(a, b):
    """Return sum of `a` and `b`."""
    return a + b


# test function with assert
assert add(3, 2) == 5

# Conclusion:
# No AssertError is raised since add(3, 2) == 5 evaluates to True. If expression after assert is False,
# an AssertError exception will be raised.
