import pytest
from conftest import load_solution

module = load_solution("misc/013_two_number_sum.py")


@pytest.mark.parametrize(
    ("array", "target", "expected"),
    [
        ([3, 5, -4, 8, 11, 1, -1, 6], 10, {11, -1}),
        ([4, 6], 10, {4, 6}),
        ([1, 2, 3], 100, set()),
        ([], 5, set()),
    ],
)
def test_two_number_sum(array, target, expected):
    assert set(module.twoNumberSum(array, target)) == expected
