# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        maxsum = 0
        for key, val in count.items():
            c = ceil(val/(key+1))
            maxsum += c *(key+1)
        return maxsum