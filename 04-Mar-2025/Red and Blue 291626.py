# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

t=int(input())
for _ in range(t):
    n=int(input())
    red=list(map(int,input().split()))
    m=int(input())
    blue=list(map(int,input().split()))
    for i in range(1,n):
        red[i]=red[i]+red[i-1]
    for j in range(1,m):
        blue[j]+=blue[j-1]
    max_red=max(red)
    max_blue=max(blue)
    max_red=max(0,max_red)  # if the prefix sum is negative use this to handle it 
    max_blue=max(0,max_blue)
    print(max_red+max_blue)



        



