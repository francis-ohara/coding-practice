import pytest
from conftest import load_solution

module = load_solution(
    "leetcode/1290_convert_binary_number_in_a_linked_list_to_integer.py"
)


def build_linked_list(values):
    head = None
    for value in reversed(values):
        head = module.ListNode(value, head)
    return head


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([1, 0, 1], 5),
        ([0], 0),
        ([1], 1),
        ([1, 1, 1, 1], 15),
    ],
)
def test_get_decimal_value(values, expected):
    head = build_linked_list(values)
    assert module.Solution().getDecimalValue(head) == expected
