# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a

def dp():
  n=int(input()) 
  arr=list(map(int,input().split()))
  if n==1:
     print(0)
     return
  dp=[float("inf")]*len(arr)
  dp[0]=0
  dp[1]=abs(arr[1]-arr[0])
  for i in range(2,len(dp)):
     dp[i]=min(dp[i-1]+abs(arr[i]-arr[i-1]),dp[i-2]+abs(arr[i]-arr[i-2]))
  print(dp[n-1])
dp()
  