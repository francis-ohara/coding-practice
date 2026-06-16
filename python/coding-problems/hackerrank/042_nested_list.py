# link: https://www.hackerrank.com/challenges/nested-list/problem

# finding the second smallest value
# case 1: current value < smallest value
# case 2: current value !< smallest value but current value < second smallest

N = int(input())  # number of students
records = [[input(), float(input())] for _ in range(N)]  # list of student names and grades

# find second-lowest grade
lowest = float("inf")
second_lowest = float("inf")
for record in records:
    if record[1] < lowest:
        second_lowest = lowest
        lowest = record[1]
    elif second_lowest > record[1] > lowest:
        second_lowest = record[1]

# find students with second-lowest grade
students = [name for name, grade in records if grade == second_lowest]
students = list(sorted(students))  # order alphabetically

# print students
for student in students:
    print(student)
