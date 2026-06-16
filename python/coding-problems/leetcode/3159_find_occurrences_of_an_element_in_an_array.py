"""
Problem: https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/
"""

class Solution:
    def occurrencesOfElement(self, nums: list[int], queries: list[int], x: int) -> list[int]:
        output = []
        occurrences = []

        for i in range(len(nums)):
            if nums[i] == x:
                occurrences.append(i)
        
        for query in queries:
            if query > len(occurrences):
                output.append(-1)
            else:
                output.append(occurrences[query - 1])
        
        return output

        

        
