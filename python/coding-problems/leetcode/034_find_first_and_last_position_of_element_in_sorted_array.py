# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = [-1, -1]

        while left <= right:
            middle = (left + right) // 2

            if target == nums[middle]:
                start = middle
                end = middle
                while start - 1 >= 0 and nums[start - 1] == target:
                    start -= 1
                while end + 1 < len(nums) and nums[end + 1] == target:
                    end += 1
                result = [start, end]
                break

            elif target < nums[middle]:
                right = middle - 1

            else:
                left = middle + 1

        return result
