# TASK
# Given a string s, find the length of the longest substring without repeating characters.
# Example: Input: s = "abcabcbb" Output: 3
# Explanation: The answer is "abc", with the length of 3.

# define function for finding longest substring
def longest_sub(string: str) -> int:
    """Return the length of the longest substring in `string` without repeating characters."""
    streaks = []  # list of longest streaks so far
    previous = []  # list of previously seen characters in current streak
    streak = 0  # current streak

    for char in string:
        if char not in previous:
            previous.append(char)
            streak += 1
        else:
            streaks.append(streak)
            streak = 1  # reset current streak
            previous = [char]  # reset previous characters

    streaks.append(streak)  # ensure streak value at end of loop is included
    return max(streaks) # return largest streak

# test the function
s = input()
print(longest_sub(s))
