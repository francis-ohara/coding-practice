# link: https://www.hackerrank.com/challenges/collections-counter/problem

# var amount_rahu_earned
# shoe_inventory = Counter()

# for next N
#   shoe_size, price = map(int, input().split())
#   if shoe_size in shoe_inventory.keys():
#       add price to amount_rahu_earned
#       decrement value of shoe_size in shoe_inventory by 1
#       if shoe_inventory[shoe_size] == 0:
#           del shoe_inventory[shoe_size]
# return amount_rahu_earned.
from collections import Counter

revenue = 0
X = int(input())
shoes = list(map(int, input().split()))
shoes_count = Counter(shoes)

N = int(input())

for customer in range(N):
    shoe_size, price = map(int, input().split())

    # if shoe is present in store
    if shoe_size in shoes_count.keys():
        revenue += price
        shoes_count[shoe_size] -= 1

        # if last shoe of that size is sold
        if shoes_count[shoe_size] == 0:
            del shoes_count[shoe_size]

print(revenue)
