# Problem: Maximum Points You Can Obtain from Cards - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left=0
        right=len(cardPoints)-k
        total=sum(cardPoints[right:])
        max_score=total
        while right <len(cardPoints):
            total+=cardPoints[left]-cardPoints[right]
            max_score=max(max_score,total)
            left+=1
            right+=1
           
        return max_score 
