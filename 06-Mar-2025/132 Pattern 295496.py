# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]
        prev=nums[0]
        for c in nums[1:]:
            while stack and  c>=stack[-1][0]:
                stack.pop()
            if stack and c >stack[-1][1]:
                    return True 
            stack.append([c,prev])
            prev=min(c,prev)
        return False 