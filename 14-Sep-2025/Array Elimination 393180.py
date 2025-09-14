# Problem: Array Elimination - https://codeforces.com/contest/1601/problem/A


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    bit_counts = [0] * 30 
    for x in a:
        for j in range(30):
            if (x >> j) & 1:  
                bit_counts[j] += 1

    possible_k = []
    for k in range(1, n + 1):
        is_k_possible = True
        for j in range(30):
            if bit_counts[j] % k != 0: 
                is_k_possible = False  
                break
        
        if is_k_possible: 
            possible_k.append(k)
    
    print(*possible_k)


t = int(input())
for _ in range(t):
    solve()