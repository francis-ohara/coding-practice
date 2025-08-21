# https://leetcode.com/problems/set-mismatch/?envType=daily-question&envId=2024-01-22


class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        answer = [0, 0]
        nums = list(sorted(nums))
        s = range(1, len(nums) + 1)
        for i in range(len(nums)):
            if (answer[1] == 0) and (nums[i] != s[i]):
                if s[i] not in nums:
                    answer[1] = s[i]
            if (i != 0) and (nums[i] == nums[i-1]):
                answer[0] = nums[i]
        return answer

