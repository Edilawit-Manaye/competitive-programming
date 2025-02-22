# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]
n, k, q = ls()
prefix = [0]* 200002
prefix2 = [0] * 200002
nums = []
que = []
for _ in range(n):
    arr = list(map(int, input().split()))
    nums.append(arr)
for _ in range(q):
    arr = list(map(int, input().split()))
    que.append(arr)

for start, end in nums:
    prefix[start] +=1
    prefix[end+1] -=1
for i in range(1, len(prefix)):
    prefix[i] += prefix[i-1]
for i in range(1, len(prefix)):
    if prefix[i] >= k:
        prefix2[i] += prefix2[i-1]+1
    else:
        prefix2[i] = prefix2[i-1]
for left, right in que:
    print(prefix2[right] - prefix2[left-1])