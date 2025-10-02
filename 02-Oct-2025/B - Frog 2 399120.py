# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

def dp():
  n,k=map(int,input().split())
  arr=list(map(int,input().split()))
  dp=[float("inf")]*len(arr)
  dp[0]=0
  for i in range(1,len(arr)):
     for j in range(max(0,i-k),i):
        dp[i]=min(dp[i],abs(arr[i]-arr[j])+dp[j])
  print(dp[-1])
dp()  
  
