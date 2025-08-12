# Problem: Young Physicist - https://codeforces.com/problemset/problem/69/A

t=int(input())
l,m,n=0,0,0
for _ in range(t):
    x,y,z=map(int,input().split())
    l,m,n=x+l,y+m,z+n
if l==0 and m==0 and n==0:
    print("YES")
else:
    print("NO")

