# link: https://www.hackerrank.com/challenges/zipped/problem

N, X = map(int, input().split())
all_scores = []
for _ in range(X):
    all_scores.append(map(float, input().split()))

for student_scores in zip(*all_scores):
    average = sum(student_scores) / X
    print(f"{average:0.1f}")
