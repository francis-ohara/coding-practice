# link: https://www.hackerrank.com/challenges/merge-the-tools/

def merge_the_tools(string, k):
    start = 0
    end = k

    for _ in range(len(string)//k):
        t = string[start:end]
        u = ""
        for char in t:
            if char not in u:
                u += char
        print(u)
        start += k
        end += k


merge_the_tools("AABCAAADA", 3)
