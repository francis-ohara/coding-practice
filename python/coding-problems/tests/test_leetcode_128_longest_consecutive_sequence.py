import pytest
from conftest import load_solution

module = load_solution("leetcode/128_longest_consecutive_sequence.py")


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([1, 0, 1, 2], 3),
        ([], 0),
        ([7], 1),
    ],
)
def test_longest_consecutive(nums, expected):
    assert module.Solution().longestConsecutive(nums) == expected
