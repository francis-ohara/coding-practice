"""Test how inheritance of attributes works in Python.

attributes for a class can either be defined in the class's scope or within the constructor for the class.
If I choose to define the attributes only within the constructor, and I override that constructor in a child class,
will the child class not have all the attributes of the parent even though it's by definition supposed to?
"""


# parent class with all attributes defined in constructor.
class Parent:
    def __init__(self):
        self.foo = "hello"
        self.bar = "world"


# child class of Parent that overrides Parent's constructor.
class Child(Parent):
    def __init__(self): # override the constructor
        self.foobar = "Bye, Earth!"


# parent = Parent()
# print(parent.foo)
#
# child = Child()
# print(child.foo)

# alternate Parent class with attributes defined within the Class's scope
class GoodParent:
    foo = "hello"
    bar = "world"


class goodChild(GoodParent):
    def __init__(self):
        foobar = "hello earth"


good_child = goodChild()
print(good_child.foo)

# Conclusion:
# The danger to defining all attributes in the constructor is that if the parent is inherited and the child overrides
# the parent's constructor then one has to manually ensure that the child has all the parent's attributes in its
# constructor. The super() built-in is useful in this situation.

