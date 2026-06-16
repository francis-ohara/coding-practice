# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/

class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        n_pairs = 0
        for j in range(len(nums)):
            for i in range(j):
                if nums[i] + nums[j] < target:
                    n_pairs += 1
        return n_pairs

