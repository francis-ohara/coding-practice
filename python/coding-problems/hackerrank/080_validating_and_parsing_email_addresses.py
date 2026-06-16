# Link: https://www.hackerrank.com/challenges/validating-named-email-addresses/problem
# Task:
# A valid email address meets the following criteria:
# • It's composed ofa username, domain name, and extension assembled in this format: username@domain.extension
# • The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the
# following: alphanumeric characters, -, . , and
# • The domain and extension contain only English alphabetical characters.
# The extension is 1, 2, or 3 characters in length.
# Given n pairs of names and email addresses as input, print each name and email address pair having a valid email address on
# a new line.
# Hint: Try using Email.utils() to complete this challenge. For example, this code:
# import email. utils
# print email. utils.parseaddr( 'DOSHI <DOSHI@hackerrank. com> ' )
# print email. uti Is. formataddr(( ' DOSHI '
# ' DOSHI@hackerrank. com ' ) )
# produces this output:
# ( ' DOSHI '
# ' DOSHI@hackerrank.com )
# DOSHI
# Input Format
# The first line contains a single integer, n, denoting the number of email address.
# Each line i of the n subsequent lines contains a name and an email address as two space-separated values following this
# format:
# name <user@email.com>
# Constraints
# • O < n < 100
# Output Format
# Print the space-separated name and email address pairs containing valid email addresses only. Each pair must be printed on a
# new line in the following format:
# name <user@email.com>
# You must print each valid email address in the same order as it was received as input.

import re

n = int(input())
regex = "^[A-Za-z][A-Za-z0-9\-\._]+@[A-Za-z]+\.[A-Za-z]{1,3}$"

for i in range(n):
    line = input()
    name, address = line.split()
    address = address.strip("<>")
    if re.search(regex, address):
        print(line)
