# https://leetcode.com/problems/number-of-good-pairs/description/

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
            n_good_pairs = 0
            for i in range(len(nums)):
                for j in range(i):
                    if nums[i] == nums[j]:
                        n_good_pairs += 1
            return n_good_pairs