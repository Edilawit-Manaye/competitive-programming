# Problem: Wrong Subtraction - https://codeforces.com/problemset/problem/977/A?mobile=false

n,k=map(int,input().split())
m=str(n)
i=0
count=int(m)
l=m
while count and l and  i <k:
    if l[-1]!="0":
        count=count-1
        l=str(count)
    else:
        count=count//10
        l=str(count)
    i+=1
print(count)
