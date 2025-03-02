# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

num_stones = int(input())
costs = list(map(int, input().split()))
num_queries = int(input())

prefix_unsorted = []
prefix_unsorted.append(costs[0])
for idx in range(1, num_stones):
    prefix_unsorted.append(costs[idx] + prefix_unsorted[idx - 1])

sorted_costs = sorted(costs)
prefix_sorted = []
prefix_sorted.append(sorted_costs[0])
for idx in range(1, num_stones):
    prefix_sorted.append(sorted_costs[idx] + prefix_sorted[idx - 1])

for _ in range(num_queries):
    query_type, left, right = map(int, input().split())
    if query_type == 1:
        result = prefix_unsorted[right - 1] - (prefix_unsorted[left - 2] if left > 1 else 0)
        print(result)
    elif query_type == 2:
        result = prefix_sorted[right - 1] - (prefix_sorted[left - 2] if left > 1 else 0)
        print(result)