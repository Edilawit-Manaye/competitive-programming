# Problem: Helpful Maths - https://codeforces.com/problemset/problem/339/A

t=input()
strr=[]
for n in t:
    if n!="+":
        strr.append(n)
strr2=[]
strr.sort()
for i in range(len(strr)):
    if i==len(strr)-1:
        strr2.append(strr[i])
    else:
        strr2.append((strr[i]) + ("+"))
print("".join(strr2))




