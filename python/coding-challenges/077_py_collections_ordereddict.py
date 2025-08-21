# link: https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
from collections import OrderedDict

N = int(input())
purchases = OrderedDict()

for _ in range(N):
    *item_name, net_price = input().split()
    item_name = " ".join(item_name)
    net_price = int(net_price)
    purchases[item_name] = purchases.get(item_name, 0) + net_price

for item_name, net_price in purchases.items():
    print(item_name, net_price)
