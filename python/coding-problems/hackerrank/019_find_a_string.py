# link: https://www.hackerrank.com/challenges/find-a-string/problem

string = input()
sub_string = input()
count = 0

for i in range(len(string) - len(sub_string) + 1):
    is_match = True
    for j in range(len(sub_string)):
        if string[i + j] != sub_string[j]:
            is_match = False

    if is_match:
        count += 1

print(count)
