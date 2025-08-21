# https://leetcode.com/problems/minimum-number-game/description/

class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        arr = []
        nums = list(sorted(nums))
        for i in range(1, len(nums), 2):
            arr.extend([nums[i], nums[i-1]])
        return arr

