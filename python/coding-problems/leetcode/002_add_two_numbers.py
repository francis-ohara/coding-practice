# https://leetcode.com/problems/add-two-numbers/description/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result = ListNode()
        current_l1 = l1
        current_l2 = l2
        current_result = result

        while True:
            total = 0
            if current_l1 is None and current_l2 is None:
                break

            elif current_l1 is None and current_l2 is not None:
                total = current_result.val + current_l2.val
                remainder = total % 10
                carry = total // 10
                current_result.val = remainder
                current_l2 = current_l2.next
                if current_l2 is not None or carry != 0:
                    current_result.next = ListNode()
                    current_result = current_result.next
                    current_result.val += carry
            elif current_l2 is None and current_l1 is not None:
                total = current_result.val + current_l1.val
                remainder = total % 10
                carry = total // 10
                current_result.val = remainder
                current_l1 = current_l1.next
                if current_l1 is not None or carry != 0:
                    current_result.next = ListNode()
                    current_result = current_result.next
                    current_result.val += carry
            else:
                total = current_result.val + current_l1.val + current_l2.val
                remainder = total % 10
                carry = total // 10
                current_result.val = remainder
                current_l1 = current_l1.next
                current_l2 = current_l2.next
                if current_l1 is not None or current_l2 is not None or carry != 0:
                    current_result.next = ListNode()
                    current_result = current_result.next
                    current_result.val += carry
        return result
