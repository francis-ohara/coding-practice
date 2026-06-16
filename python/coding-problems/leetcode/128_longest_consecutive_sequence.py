"""
Problem: https://leetcode.com/problems/longest-consecutive-sequence/
"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        all_nums = set()
        min = nums[0]
        max = nums[0]
        previous_num = min
        streak = 1
        max_streak = 1

        for num in nums:
            all_nums.add(num)
            if num < min:
                min = num
            if num > max:
                max = num

        for current_num in range(min, max + 1):
            if current_num in all_nums:
                if current_num  - 1 == previous_num:
                    streak += 1
                    if streak > max_streak:
                        max_streak = streak
                else:
                    streak = 1
                previous_num = current_num

        return max_streak
            