# Problem: Watermelon - https://codeforces.com/problemset/problem/4/A

n=int(input())
is_first= False
for i in range (1,n-1):
    if i%2==0 and (n-i)%2==0:
        is_first=True
        break
if is_first:
    print("YES")
else:
    print("NO")
