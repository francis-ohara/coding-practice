# https://www.hackerrank.com/challenges/matching-specific-string/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

Regex_Pattern = r'hackerrank'	# Do not delete 'r'.

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))