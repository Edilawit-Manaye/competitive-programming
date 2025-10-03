# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c

def maxx():
    n = int(input())
    listt = []
    for i in range(n):
        arr = list(map(int, input().split()))
        listt.append(arr)
    
    dp = [[0] * 3 for _ in range(n)] 
    dp[0] = listt[0]

    for r in range(1, n):
        for c in range(3):
            if c == 0:
                dp[r][c] = listt[r][c] + max(dp[r-1][1], dp[r-1][2])  
            elif c == 1:
                dp[r][c] = listt[r][c] + max(dp[r-1][0], dp[r-1][2])  
            elif c == 2:
                dp[r][c] = listt[r][c] + max(dp[r-1][0], dp[r-1][1])  

    print(max(dp[-1]))

maxx()