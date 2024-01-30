# https://leetcode.com/problems/count-items-matching-a-rule/description/

class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        n_valid_items = 0
        attribute_mapper = {"type": 0, "color": 1, "name": 2}

        for item in items:
            if item[attribute_mapper[ruleKey]] == ruleValue:
                n_valid_items += 1

        return n_valid_items