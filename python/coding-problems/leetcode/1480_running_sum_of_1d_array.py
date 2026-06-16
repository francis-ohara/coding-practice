# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        increment = 0
        for i in range(len(nums)):
            increment += nums[i]
            nums[i] = increment
        return nums