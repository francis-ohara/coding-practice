# https://app.codesignal.com/arcade/intro/level-2/xzKiBHjhoinnpdh6m


def solution(inputArray):
    largest = inputArray[0] * inputArray[1]
    for i in range(len(inputArray) - 1):
        product = inputArray[i] * inputArray[i + 1]
        if product > largest:
            largest = product
    return largest