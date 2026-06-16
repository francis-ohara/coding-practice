# https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = accounts[0][0]
        for customer in accounts:
            customer_wealth = 0
            for balance in customer:
                customer_wealth += balance
            if customer_wealth > max_wealth:
                max_wealth = customer_wealth
        return max_wealth