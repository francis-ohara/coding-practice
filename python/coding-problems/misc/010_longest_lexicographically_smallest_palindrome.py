"""
### Problem Description

You're developing a new programming language with some unusual features for strings! Among these is a method that returns the longest palindrome that can be formed with the characters of a given string.

Given a string `s`, your task is to find this **longest possible palindrome**. You may use any number of the characters from `s`, and arrange them in any order (so long as it results in a palindrome).

If there are multiple longest palindromes that can be formed, return the one among them that's **lexicographically smallest**.

### Examples

* For `s = "aaabb"`, the output should be `solution(s) = "ababa"`.
* There are two possible palindromes of length 5 that can be obtained (`"ababa"` and `"baaab"`), but `"ababa"` is lexicographically smaller, thus it is the answer.


* For `s = "aaabbbcc"`, the output should be `solution(s) = "abcacba"`.
* It's not possible to form a palindrome of length 8, but from several palindromes of length 7, `"abcacba"` is the lexicographically smallest, thus it is the answer.



### Input/Output

* **[execution time limit]** 4 seconds (py3)
* **[memory limit]** 1 GB
* **[input] string s**
* The given string.
* **Guaranteed constraints:** 


* **[output] string**
* The lexicographically smallest palindrome with maximal length that can be built from the given string `s`.
"""

def solution(s):
    s_histogram = {}
    for char in s:
        s_histogram[char] = s_histogram.get(char, 0) + 1
    
    left_wing = ""
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for alphabet in alphabets:
        if s_histogram.get(alphabet):
            left_wing += alphabet * (s_histogram[alphabet] // 2)

    center = ""
    for char in s_histogram:
        if s_histogram[char] % 2 == 1:
            if center == "":
                center = char
            elif char < center:
                center = char

    return left_wing + center + left_wing[::-1]


