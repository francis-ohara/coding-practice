# https://www.algoexpert.io/questions/sorted-squared-array

def sortedSquaredArray(array):
    squares = []
    for value in array:
        squares.append(value ** 2)
    return list(sorted(squares))
