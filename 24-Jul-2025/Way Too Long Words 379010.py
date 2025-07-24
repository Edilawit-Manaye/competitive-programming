# Problem: Way Too Long Words - https://codeforces.com/problemset/problem/71/A

n=int(input())
alll=[]
for _ in range (n):
    wordd=input()
    if len(wordd)<=10:
        alll.append(wordd)
        
    else:
        strr=""
        strr+=(wordd[0])
        strr+=(str(len(wordd)-2))
        strr+=(wordd[len(wordd)-1])
        alll.append(strr)

        
for l in alll:
    print(l)
            
    