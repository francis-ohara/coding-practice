# https://app.codesignal.com/arcade/intro/level-1/s5PbmwxfECC52PWyQ

def solution(inputString):
    for i in range(len(inputString) // 2):
        if inputString[i] != inputString[len(inputString)-1-i]:
            return False
    return True
