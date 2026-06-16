# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        results = []
        for i in range(len(nums)):
            n_less_than = 0
            for j in range(len(nums)):
                if i != j and nums[j] < nums[i]:
                    n_less_than += 1
            results.append(n_less_than)
        return results

