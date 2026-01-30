"""Test what happens when an attribute of an object is assigned to a variable.
Does the variable contain a copy of the value of that attribute or a reference to the location of the attribute in
memory? I.e. Can the variable be used to modify the content of the attribute of the object?
"""

class Bar:
    attribute = 42

    def method(self, greeting):
        var1 = self.attribute
        var1 = greeting
        print("method called!")

bar = Bar()

var = bar.attribute
print(f"Var: {var}\nbar.attribute: {bar.attribute}")

var = 35
print(f"Var: {var}\nbar.attribute: {bar.attribute}")

var = "hello"
bar.method(var)
print(f"Var: {var}\nbar.attribute: {bar.attribute}")


"""Conclusion:
When an attribute of an object is assigned to a variable, only a copy of the attribute's value is assigned to the 
variable, not a reference to the attribute in memory.
"""