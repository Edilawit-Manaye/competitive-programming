# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

import sys
 
ipt = sys.stdin.readline
t = int(ipt())
 
for _ in range(t):
    n = int(ipt())
    arr = list(map(int, ipt().split()))
 
    size = len(arr)
    left = 0
    right = 0
    max_count = 0
    count = arr[left]
 
    while right < size:
        # end of the list with multiple consecutive element
        if arr[left] * arr[right] > 0 and right == size - 1:
            max_count += max(count, arr[right])
        elif arr[left] * arr[right] > 0:
            count = max(count, arr[right])
        else:
            max_count += count
            count = arr[right]
            left = right
        right += 1
        # Handle the case of last two elements having different sign
        if right == size - 1 and arr[left] * arr[right] < 0:
            max_count += arr[right]
 
    print(max_count)