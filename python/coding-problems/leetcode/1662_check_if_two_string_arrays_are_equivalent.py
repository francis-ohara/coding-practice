# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        built_word1 = ""
        for word in word1:
            for char in word:
                built_word1 += char

        index = 0

        for word in word2:
            for char in word:
                if index == len(built_word1) or char != built_word1[index]:
                    return False
                index += 1

        if len(built_word1) != index:
            return False

        return True
