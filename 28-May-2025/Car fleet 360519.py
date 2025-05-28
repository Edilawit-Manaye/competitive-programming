# Problem: Car fleet - https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted(zip(position, speed), reverse=True)
        stack = []
        
        for p, s in pair:
            time = (target - p) / s
            
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)

