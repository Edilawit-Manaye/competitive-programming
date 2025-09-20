# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

t = int(input())
for _ in range(t):
    x = int(input())
    count=bin(x).count("1")
    y=x&-x
    if count==1 and x==1: 
        y|=2
    elif count==1 :
        y|=1
    print(y)

    
