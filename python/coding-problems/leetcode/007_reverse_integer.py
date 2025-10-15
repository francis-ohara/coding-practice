# https://leetcode.com/problems/reverse-integer/?envType=company&envId=linkedin&favoriteSlug=linkedin-six-months

class Solution:
    def reverse(self, x: int) -> int:
        result = ""

        if x < 0:
            result += "-"
            x = x * -1
        
        result += str(x)[::-1]
        integer_result = int(result)

        if integer_result <  -(2 ** 31) or integer_result >= 2 ** 31:
            return 0
        
        return integer_result