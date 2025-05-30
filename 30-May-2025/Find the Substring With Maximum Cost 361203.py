# Problem: Find the Substring With Maximum Cost - https://leetcode.com/problems/find-the-substring-with-maximum-cost/

class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        char_values = [i + 1 for i in range(26)]

        for i in range(len(chars)):
            char_index = ord(chars[i]) - ord('a')
            char_values[char_index] = vals[i]

        max_sum_ending_here = 0
        max_sum_so_far = 0

        for char_s in s:
            cost = char_values[ord(char_s) - ord('a')]
            max_sum_ending_here += cost
            
            if max_sum_ending_here < 0:
                max_sum_ending_here = 0
            
            max_sum_so_far = max(max_sum_so_far, max_sum_ending_here)
            
        return max_sum_so_far