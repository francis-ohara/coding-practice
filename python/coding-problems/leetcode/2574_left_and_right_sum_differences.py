# https://leetcode.com/problems/left-and-right-sum-differences/

class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        left_sum = 0
        right_sum = 0
        for i in range(1, len(nums)):
            right_sum += nums[i]
        result = [abs(left_sum - right_sum)]

        for i in range(1, len(nums)):
            left_sum += nums[i - 1]
            right_sum -= nums[i]
            result.append(abs(left_sum - right_sum))
        return result