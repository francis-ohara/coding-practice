# https://leetcode.com/problems/number-of-employees-who-met-the-target/

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
            n_qualified = 0
            for hour in hours:
                if hour >= target:
                    n_qualified += 1
            return n_qualified
