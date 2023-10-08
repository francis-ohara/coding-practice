"""Test Python 3.10's match case feature: The equivalent of switch case statements in Python"""

var = 42

match var:
    case 37:
        print("hello")

    case 42:
        print("world")

    case 43:
        print("Bye")

    case _:
        print("Earth")

"""
Conclusion:
The match-case syntax can be used to implement switch-case statements in Python.
`match` and `case` are soft keywords that were introduced into Python in Python 3.10.
They are soft keywords in that they can be used as identifiers when the parser does not detect that they are being used in the match-case syntax.
Actual keywords however can never be used as identifiers.

Additionally, match-case in Python only runs the block of code for the matched case.
Therefore, no break statement is necessary and no fallthrough errors can occur with match-case statements in Python.
"""