# https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        result = [0 for i in range(len(s))]

        for i in range(len(s)):
            result[indices[i]] = s[i]

        return "".join(result)
