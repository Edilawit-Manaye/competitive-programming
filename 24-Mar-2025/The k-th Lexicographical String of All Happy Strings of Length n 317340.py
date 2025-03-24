# Problem: The k-th Lexicographical String of All Happy Strings of Length n - https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy_strings = []
        
        def backtrack(current_string):
            if len(current_string) == n:
                happy_strings.append(current_string)
                return
            
            last_char = current_string[-1] if current_string else ''
            for char in 'abc':
                if char != last_char:
                    backtrack(current_string + char)
        
        backtrack('')
        
        return happy_strings[k - 1] if k <= len(happy_strings) else ''