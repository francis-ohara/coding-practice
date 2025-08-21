# link: https://www.hackerrank.com/challenges/python-time-delta/problem

from time import strptime
from calendar import timegm


def time_delta(t1: str, t2: str) -> str:
    """Returns the difference in seconds between two times `t1` and `t2` which are specified using the format
    Day dd Mon yyyy hh:mm:ss +xxxx."""
    unix_time_1 = to_unix(t1)
    unix_time_2 = to_unix(t2)
    return str(abs(unix_time_1 - unix_time_2))


def to_unix(str_t: str) -> int:
    """Accepts a string containing a date and time, in the format Day dd Mon yyyy hh:mm:ss +xxxx, and returns its
    equivalent in unix time."""
    day_of_week, *date_time, timezone = str_t.split()
    date_time_str = " ".join(date_time)
    tuple_t = strptime(date_time_str, "%d %b %Y %H:%M:%S")
    unix_t = timegm(tuple_t)

    # convert unix_t based on timezone
    hours = int(timezone[1:3])
    minutes = int(timezone[3:])
    time_zone_difference = (hours * 3600) + (minutes * 60)
    time_zone_difference = (time_zone_difference * -1) if (timezone[0] == "+") else time_zone_difference

    # add time zone difference to unix_t
    unix_t += time_zone_difference
    return unix_t


print(time_delta("Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000"))
