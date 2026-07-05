import pytest
from conftest import load_solution

module = load_solution("misc/014_validate_subsequence.py")


@pytest.mark.parametrize(
    ("array", "sequence", "expected"),
    [
        ([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10], True),
        ([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10], True),
        ([5, 1, 22, 25, 6, -1, 8, 10], [22, 25, 6], True),
        ([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, 10, -1], False),
        ([5, 1, 22, 25, 6, -1, 8, 10], [26], False),
    ],
)
def test_is_valid_subsequence(array, sequence, expected):
    assert module.isValidSubsequence(array, sequence) == expected
