# Problem: Serval and The Formula - https://codeforces.com/problemset/problem/2085/C

t=int(input())
for _ in range(t):
    m,n=map(int,input().split())
    if m==n:
        print(-1)
        continue
    if m^n==m+n:
        print(0)
        continue
    b=max(m,n)
    p=1
    while p<=b:
        p<<=1
    k=p-b
    print(k)