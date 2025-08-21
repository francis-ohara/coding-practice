# link: https://www.hackerrank.com/challenges/swap-case/problem

import sys
def swap_case_1(s):
    """Returns string `s` with all uppercase alphabets as lowercase alphabets and all lowercase alphabets as uppercase alphabets.
    Uses my initial Python dictionary approach :)
    """
    result = []
    toggler = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i',
               'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r',
               'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z', 'a': 'A',
               'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J',
               'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S',
               't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}

    for char in s:
        if char in toggler:
            result.append(toggler[char])
        else:
            result.append(char)
    return "".join(result)


def swap_case_2(s):
    """Returns string `s` with all uppercase alphabets as lowercase alphabets and all lowercase alphabets as uppercase alphabets.
    Uses ASCII value manipulation approach."""
    result = []
    for char in s:
        ascii_ch = ord(char)
        if 90 >= ascii_ch >= 65:
            result.append(chr(ascii_ch + 32))
        elif 122 >= ascii_ch >= 97:
            result.append(chr(ascii_ch - 32))
        else:
            result.append(char)
    return "".join(result)


print(swap_case_1("mICKEY mOUSE"))
print(swap_case_2("mICKEY mOUSE"))

