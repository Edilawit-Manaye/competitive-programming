# Problem: Dictionary - https://codeforces.com/problemset/problem/1674/B

import sys; from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right; from random import randint; from itertools import accumulate

def numi(): return int(sys.stdin.readline().strip())
def numsi(): return list(map(int, sys.stdin.readline().strip().split()))
def wordi(): return sys.stdin.readline().strip()
def map_int(): return map(int, sys.stdin.readline().strip().split())
def map_str(): return map(str, sys.stdin.readline().strip().split())
def test(input=0): return numi() if not input else input
def yn(condition): print("YES" if condition else "NO")
def prefix_sum(arr): return list(accumulate(arr))
def Counter(a): return (lambda d: ([(d.__setitem__(xor(x), d.get(xor(x), 0) + 1)) for x in a], d)[1])(defaultdict(int))
rand = randint(1, int(1e9)); xor = lambda x: x ^ rand

def solve():
    s = wordi()
    a, b = s[0], s[1]
    
    a = ord(a) - ord('a') 
    b = ord(b) - ord('a')
    # print(a, b, a * b)
    
    if b < a:
        print(((25 * a) + b + 1))
    else: 
        print(((25 * a) + b))


for _ in range(test()):
    solve()