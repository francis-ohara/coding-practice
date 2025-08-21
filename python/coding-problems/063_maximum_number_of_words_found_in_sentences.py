# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 1
        for sentence in sentences:
            n_words = 1
            for char in sentence:
                if char == " ":
                    n_words += 1
            if n_words > max_words:
                max_words = n_words
        return max_words
