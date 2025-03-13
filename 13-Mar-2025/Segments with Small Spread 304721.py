# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque

n, k = map(int, input().split())
array = list(map(int, input().split()))
ans = 0
left = 0
maximum_queue = deque()
minimum_queue = deque()

for right in range(n):
    while maximum_queue and array[right] > maximum_queue[-1]:
        maximum_queue.pop()
    maximum_queue.append(array[right])
    while minimum_queue and array[right] < minimum_queue[-1]:
        minimum_queue.pop()
    minimum_queue.append(array[right])

    while maximum_queue and minimum_queue and (maximum_queue[0] - minimum_queue[0] > k):
        if array[left] == maximum_queue[0]:
            maximum_queue.popleft()
        if array[left] == minimum_queue[0]:
            minimum_queue.popleft()
        left += 1
    
    ans+=(right-left+1)

print(ans)
