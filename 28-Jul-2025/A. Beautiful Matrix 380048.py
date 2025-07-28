# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

matrix=[]
for _ in range(5):
    matrix.append(list(map(int,input().split())))
count=0
for r in range(5):
    for c in range(5):
        if matrix[r][c]==1:
            count+=abs(r-2)+abs(c-2)
            break
print(count)
