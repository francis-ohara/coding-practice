# https://leetcode.com/problems/build-array-from-permutation/description/

class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans
