# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict
n, k = map(int, input().split())
arr = list(map(int, input().split()))
count=defaultdict(int)
l=0
left_index,right_index=0,0
for r in range(n):
    count[arr[r]]+=1
    while len(count)>k:
        count[arr[l]]-=1
        if count[arr[l]]==0:
            del count[arr[l]]
        l+=1
    if (r-l)>(right_index-left_index):
        left_index,right_index=l,r
print(left_index+1,right_index+1)

    

