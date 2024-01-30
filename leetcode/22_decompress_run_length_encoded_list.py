# https://leetcode.com/problems/decompress-run-length-encoded-list/description/

class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(((len(nums) - 2) // 2) + 1):
            freq, val = nums[2 * i], nums[(2 * i) + 1]
            result.extend([val for i in range(freq)])
        return result
