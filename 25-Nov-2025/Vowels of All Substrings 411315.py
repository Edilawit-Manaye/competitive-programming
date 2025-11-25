# Problem: Vowels of All Substrings - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        vowels = {"a", "e", "i", "o", "u"}
        def appears(i):
            return (i + 1) * (n - i)
       
        ans = 0
        for i in range(n):
            if word[i] in vowels:
                ans += appears(i)
        return ans
                 