# Problem: Running Miles - https://codeforces.com/problemset/problem/1826/D

t = int(input())  
for _ in range(t):  
    n = int(input())  
    arr = list(map(int, input().split()))  
    prefix = [0] * n  
    prefix[0] = arr[0] + 0  
    for i in range(1, n):  
        prefix[i] = max(prefix[i-1], arr[i] + i)  
    suffix = [0] * n  
    suffix[n-1] = arr[n-1] - (n-1)  
    for i in range(n-2, -1, -1):  
        suffix[i] = max(suffix[i+1], arr[i] - i)  

    left = 0  
    right = n - 1  
    while left < right:  
        if left + 1 < n and arr[left + 1] > arr[left]:  
            left += 1  
        else:  
            break  
    while right > 0:  
        if right - 1 >= 0 and arr[right - 1] > arr[right]:  
            right -= 1  
        else:  
            break  

    maxx = float('-inf')  
    for i in range(1, n - 1):  
        maxx = max(maxx, prefix[i-1] + suffix[i+1] + arr[i])  
    print(maxx)  
