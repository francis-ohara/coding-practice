"""Test whether Python passes by value or by reference."""


# test for basic data types (int)
def double(num):
    num *= 2
    print("num:", num)


number = 34
double(number)
print("number:", number)


# test for compound data types (list)
def doubler(numlist):
    for i in range(len(numlist)):
        numlist[i] *= 2
    print("numlist:", numlist)


numbers_list = [1, 2, 3, 4]
doubler(numbers_list)
print("numbers_list:", numbers_list)

# Conclusion:
# Depends on whether the argument is mutable or immutable.
# Immutable data types are passed by value, but mutable data types are passed by reference.
