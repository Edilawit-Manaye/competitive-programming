# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
       strr=[i+1 for i in range(n)]
       i=0
       while len(strr)>1:
            l=(i+(k-1)) % len(strr)
            strr.pop(l)
            i=l
       return strr[0]


