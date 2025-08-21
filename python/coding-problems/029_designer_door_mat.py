# link: https://www.hackerrank.com/challenges/designer-door-mat/problem

N, M = map(int, (input().split()))
pattern = ".|."
n_patterns = 1

# initial loop
for _ in range(N//2):
    print((pattern * n_patterns).center(M, "-"))
    n_patterns += 2

n_patterns -= 2

# print welcome
print("WELCOME".center(M, "-"))

# final loop
for _ in range(N//2):
    print((pattern * n_patterns).center(M, "-"))
    n_patterns -= 2
