# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

t=int(input())
for _ in range(t):
    ans=[]
    n,m=map(int,input().split())
    for _ in range(n):
        ans.append(list(map(int,input().split())))
    main_diagonal={}  #  stores the sum from topleft to bottom right the key which is i-j is the same 
    secondary_diagonal={} #  stores the sum from top rightto bottom left the key which is i+j is the same
    
    for i in range(n):
        for j in range(m):
           if i-j not in main_diagonal:
                main_diagonal[i-j]=0   # initialize 
           if i+j not in secondary_diagonal:
                secondary_diagonal[i+j]=0
           main_diagonal[i-j]+=ans[i][j]
           secondary_diagonal[i+j]+=ans[i][j]
    max_sum=float("-inf")
    for i in range(n):
        for j in range(m):
            summ=main_diagonal[i-j]+secondary_diagonal[i+j]-ans[i][j] # because ans[i][j] value occurs twice so it must be decreased
            max_sum=max(max_sum,summ)
    print(max_sum)
            




