# Problem: Experience - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/C

def find(x, parent):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x, y, parent, size, score):
    parx = find(x, parent)
    pary = find(y, parent)
    if parx != pary:
        if size[parx] < size[pary]:
            parent[parx] = pary
            score[parx] -= score[pary]
            size[pary] += size[parx]
        else:
            parent[pary] = parx
            score[pary] -= score[parx]
            size[parx] += size[pary]

def add(x, amount, parent, score):
    par = find(x, parent)
    score[par] += amount

def get(x, parent, score):
    ans = score[x]
    while x != parent[x]:
        x = parent[x]
        ans += score[x]
    return ans

def solve():
    n, q = map(int, input().split())
    parent = [i for i in range(n + 1)]
    size = [1] * (n + 1)
    score = [0] * (n + 1)

    for _ in range(q):
        query = input().split()
        if query[0] == "add":
            add(int(query[1]), int(query[2]), parent, score)
        elif query[0] == "join":
            union(int(query[1]), int(query[2]), parent, size, score)
        else:
            print(get(int(query[1]), parent, score))

solve()