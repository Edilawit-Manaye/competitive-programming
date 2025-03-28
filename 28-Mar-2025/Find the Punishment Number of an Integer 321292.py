# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def punishmentNumber(self, n: int) -> int:
        def backtrack(start: int, current_sum: int) -> bool:
            if start == len(square_str):
                return current_sum == target
            
            num = 0
            for end in range(start, len(square_str)):
                num = num * 10 + int(square_str[end])  # Build the number from the string
                if backtrack(end + 1, current_sum + num):
                    return True
            
            return False

        total_sum = 0
        
        for i in range(1, n + 1):
            square_str = str(i * i)
            target = i
            if backtrack(0, 0):  # Start backtracking from the beginning of the square string
                total_sum += i * i
        
        return total_sum

