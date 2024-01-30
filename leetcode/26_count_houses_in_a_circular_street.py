# https://leetcode.com/problems/truncate-sentence/description/

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        result = ""
        n_words = 0
        for char in s:
            if char == " ":
                n_words += 1
                if n_words == k:
                    return result
            result += char
        return result
