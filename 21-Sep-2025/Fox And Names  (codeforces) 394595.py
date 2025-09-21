# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C



from collections import defaultdict, deque 
def solve():
    n = int(input()) 
    words = []      
    for i in range(n):
        word = input()
        words.append(word)
    
    precedes = defaultdict(list) 
    indegree = defaultdict(int)  
    for i in range(1, n):    
        prev, curr = words[i-1], words[i]    
        
        for j in range(min(len(prev), len(curr))): 
            if prev[j] != curr[j]: 
                precedes[prev[j]].append(curr[j]) 
                indegree[curr[j]] += 1
                break 
        else: 
            if len(prev) > len(curr): 
                print("Impossible") 
                return
    queue = deque()  
    for i in range(26):
        ch = chr(i + 97)        
        if indegree[ch] == 0:      
            queue.append(ch)
            
    ans = []    
    
    while queue: 
        letter = queue.popleft() 
        ans.append(letter)      
        
        for neigh in precedes[letter]: 
            indegree[neigh] -= 1       
            if indegree[neigh] == 0:    
                queue.append(neigh)     
    if len(ans) < 26:  
        print("Impossible") 
    else: 
        print("".join(ans)) 

solve() 
    

    