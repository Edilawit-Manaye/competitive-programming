# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

n , k = map(int, input().split())
arr = list(map(int, input().split()))
res = []
summ = 0
for i in range(n-1):
    res.append(-arr[i+1] +arr[i])
res.sort()
for i in range(k-1):
    summ += res[i]
print(summ - arr[0] + arr[n-1])