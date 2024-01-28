# https://leetcode.com/problems/find-words-containing-character/description/

class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        word_indices = []
        for i in range(len(words)):
            if x in words[i]:
                word_indices.append(i)
        return word_indices