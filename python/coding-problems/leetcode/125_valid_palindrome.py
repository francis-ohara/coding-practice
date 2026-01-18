# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed_s = ""
    
        for char in s:
            char = char.lower()
            if char.isalnum():
                processed_s += char

        for i in range(len(processed_s) // 2):
            print(i, len(processed_s) - 1 - i)
            if processed_s[i] != processed_s[len(processed_s) - 1 - i]:
                return False
    
        return True

class Solution2: 
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].lower().isalnum():
                left += 1
                continue
            elif not s[right].lower().isalnum():
                right -= 1
                continue
            elif s[left] != s[right]:
                return False
        return True