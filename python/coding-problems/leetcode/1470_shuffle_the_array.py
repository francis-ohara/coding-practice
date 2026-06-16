# https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        result = []
        for i in range(2*n):
            # even
            if i % 2 == 0:
                result.append(nums[i // 2])
            # odd
            else:
                result.append(nums[(i // 2) + n])
        return result
