# https://leetcode.com/problems/create-target-array-in-the-given-order/

class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        target = [-1 for i in range(len(nums))]

        for i in range(len(nums)):
            if target[index[i]] == -1:
                target[index[i]] = nums[i]
            else:
                previous = target[index[i]]
                target[index[i]] = nums[i]
                for j in range(index[i] + 1, len(target)):
                    temp = target[j]
                    target[j] = previous
                    previous = temp
        return target
