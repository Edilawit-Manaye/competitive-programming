# Problem: Skibidus and Fanum Tax (hard version) - http://codeforces.com/problemset/problem/2065/C2

import bisect

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()

    prefix_max = -float('inf')
    
    for x in a:
        current_min_choice = float('inf')

        if x >= prefix_max:
            current_min_choice = x

        target_b = prefix_max + x
        idx = bisect.bisect_left(b, target_b)

        if idx < m:
            op_value = b[idx] - x
            current_min_choice = min(current_min_choice, op_value)

        if current_min_choice == float('inf'):
            print("NO")
            return
        
        prefix_max = current_min_choice
        
    print("YES")


t = int(input())
for _ in range(t):
    solve()