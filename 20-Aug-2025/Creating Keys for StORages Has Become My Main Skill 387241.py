# Problem: Creating Keys for StORages Has Become My Main Skill - https://codeforces.com/contest/2072/problem/C

t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    xorr=0
    result=[]
    for i in range(n-1):
        xorr=xorr ^ i
        result.append(i)
    last_number =xorr ^ x
    result.append(last_number)
    print(*result)
