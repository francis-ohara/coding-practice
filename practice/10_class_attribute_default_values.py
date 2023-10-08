"""Test how default attribute values for classes work in Python"""


class Bar:
    attribute_1 = "Hello"
    attribute_2 = "World!"

    def __init__(self, response):
        self.attribute_3 = response


bar = Bar("Good Earth!")
print(bar.attribute_1)


"""
Conclusion: Defining a variable/attribute outside the constructor is equivalent to setting the default value for 
that attribute. 
We don't necessarily have to define each of our attributes before calling the constructor as 
attributes can have their initial definition inside the constructor or any other method for that matter.
So the reason why we do this is to set default values for the attributes.
 """
