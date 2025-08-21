# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
            k = 0
            insertion_ptr = 0
            for i in range(len(nums)):
                if nums[i] != val:
                    k += 1
                    nums[insertion_ptr] = nums[i]
                    insertion_ptr += 1
            return k