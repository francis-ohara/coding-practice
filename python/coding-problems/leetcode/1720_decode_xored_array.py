# https://leetcode.com/problems/decode-xored-array/

class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        result = [first]
        previous = first
        for i in range(len(encoded)):
            current = encoded[i] ^ previous
            result.append(current)
            previous = current
        return result
