# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        last_unique_value = nums[0]
        insertion_index = 0
        k = 1
        for i in range(len(nums)):
            if nums[i] != last_unique_value:
                k += 1
                insertion_index += 1
                last_unique_value = nums[i]
                nums[i] = nums[insertion_index]
                nums[insertion_index] = last_unique_value
        return k
