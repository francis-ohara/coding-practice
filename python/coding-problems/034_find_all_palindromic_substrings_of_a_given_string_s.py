# https://www.youtube.com/watch?v=AdG_3GRDUfI

def is_palindrome(s: str) -> bool:
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True


def count_palindromic_substrings(s: str) -> int:
    result = 0
    for start in range(len(s)):
        for end in range(len(s), start, -1):
            substring = s[start: end]
            if is_palindrome(substring):
                result += 1

    return result


print(count_palindromic_substrings("aaa"))
