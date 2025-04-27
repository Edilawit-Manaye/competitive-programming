# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]: 
        red=defaultdict(list) 
        blue=defaultdict(list) 
        for a,b  in redEdges:
            red[a].append(b) 
        for a,b  in blueEdges:
            blue[a].append(b) 
        queue=deque()
        queue.append((0,0,None))
        answer=[-1]*n
        visit=set((0,None))
        while queue:
            node,length,edgeColor=queue.popleft()
            if answer[node]==-1:
                answer[node]=length
            if edgeColor!="RED":
                for neigh in red[node]:
                    if (neigh,"RED") not in visit:
                        visit.add((neigh,"RED"))
                        queue.append((neigh,length+1,"RED"))
            if edgeColor!="BLUE":
                for neigh in blue[node]:
                    if (neigh,"BLUE") not in visit:
                        visit.add((neigh,"BLUE"))
                        queue.append((neigh,length+1,"BLUE"))
        return answer 
        
      



        
        