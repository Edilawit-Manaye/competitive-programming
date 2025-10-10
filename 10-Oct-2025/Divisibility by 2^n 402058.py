# Problem: Divisibility by 2^n - https://codeforces.com/contest/1744/problem/D

def countTwos(n, d):
    if n % d: return 0
    
    return 1 + countTwos(n, d * 2)

for _ in range(int(input())):
    l = int(input())
    nums = list(map(int, input().split()))

    s = []
    n = a = o = 0

    for i in range(l):
        if nums[i] % 2:
            n += 1
        else:
            twosCount = countTwos(nums[i], 2)
            
            if twosCount > 1:
                a += twosCount - 1
                
            
        twosCount = countTwos(i + 1, 2)
        
        if twosCount >= 1:
            s.append(twosCount) 
            
            
    n -= a     

    if n <= 0:
        print(o)
    else:          
        s.sort(reverse=True)
        
        for sp in s:
            if n <= 0:
                break
            
            n -= sp
            o += 1
            
            
        if n <= 0:
            print(o)
        else:
            print(-1)