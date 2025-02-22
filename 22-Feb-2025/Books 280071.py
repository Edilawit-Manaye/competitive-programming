# Problem: Books - https://codeforces.com/contest/279/problem/B

n, t = map(int, input().split())
book_times = list(map(int, input().split()))


l=r=_sum=0
max_len = 0
while r < n:
    _sum+=book_times[r]
    while _sum > t:
        _sum-=book_times[l]
        l+=1
    
    max_len = max(max_len, r-l+1)
    r+=1

print(max_len)