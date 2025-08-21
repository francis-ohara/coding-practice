# link: https://www.hackerrank.com/challenges/finding-the-percentage/problem

# loop through marks array
#   increment count variable by 1
#   increment total variable by current value in array

n = int(input())  # no. of students
students = {}  # all student names and grades

# get all student names and grades
for _ in range(n):
    student = input().split()
    std_name = student[0]
    std_grades = list(map(float, student[1:]))
    students[std_name] = std_grades

# get desired student's name and grades
query_name = input()
grades = students[query_name]

# calculate average
total = 0
count = 0

for grade in grades:
    total += grade
    count += 1

avg = total / count
print(f"{avg:.2f}")  # print average correct to 2 d.p.

