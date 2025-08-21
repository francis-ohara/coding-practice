# link: https://www.hackerrank.com/challenges/calendar-module/problem

from calendar import weekday

weekdays = {
    0: "MONDAY",
    1: "TUESDAY",
    2: "WEDNESDAY",
    3: "THURSDAY",
    4: "FRIDAY",
    5: "SATURDAY",
    6: "SUNDAY"
}
month, day, year = map(int, input().split())
day_of_week = weekday(year, month, day)
print(weekdays[day_of_week])
