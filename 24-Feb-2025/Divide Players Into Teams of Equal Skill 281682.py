# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left=0
        right=len(skill)-1
        total_sum=skill[left]+skill[right]  # because to create equal skill it must be cross the smallest and the largest value together 
        ans=0
        while left<right:
            current_sum=skill[left]+skill[right]
            if current_sum!=total_sum:
                return -1
            else:
                ans+=skill[left]*skill[right]
            left+=1
            right-=1
        return ans 
            