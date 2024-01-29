# https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/description/

class Solution:
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        sum = 0
        for i in range(len(nums)):
            binary = bin(i)
            n_set_bits = 0
            for char in binary[2:]:
                if char == "1":
                    n_set_bits += 1
            if n_set_bits == k:
                sum += nums[i]
        return sum
