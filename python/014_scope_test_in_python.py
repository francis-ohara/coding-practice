# Test if it is possible to refer to a variable whose only definition is in a conditional statement's scope.

for i in range(7):
    if i == 2:
        something = True

    elif i == 5:
        print(something)

# --CONCLUSION--
# It's possible to do so in Python but not in Java.