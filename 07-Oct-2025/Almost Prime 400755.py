# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

def almost_prime(i):
    d=2
    factors=[]
    while d<=i:
        while i%d==0:
          factors.append(d)
          i//=d
        d+=1
    return len(set(factors))
count=0
n=int(input())
for i in range(1,n+1):
    if almost_prime(i)==2:
     count+=1
print(count)

