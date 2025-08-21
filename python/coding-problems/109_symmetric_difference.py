# link: https://www.hackerrank.com/challenges/symmetric-difference/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    m = int(input())
    M = set(map(int, input().split()))
    n = int(input())
    N = set(map(int, input().split()))

    for elem in sorted(M.difference(N).union(N.difference(M))):
        print(elem)
