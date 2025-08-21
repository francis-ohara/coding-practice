# https://www.algoexpert.io/questions/two-number-sum

def twoNumberSum(array, targetSum):
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j:
                if array[i] + array[j] == targetSum:
                    return [array[i], array[j]]
    return []
