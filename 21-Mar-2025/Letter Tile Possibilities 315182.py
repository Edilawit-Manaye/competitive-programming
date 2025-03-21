# Problem: Letter Tile Possibilities - https://leetcode.com/problems/letter-tile-possibilities/description/

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        letter_count = Counter(tiles)
        self.result = 0
        
        def backtrack(remaining_count):
            for letter in remaining_count:
                if remaining_count[letter] > 0:
                    self.result += 1
                    remaining_count[letter] -= 1
                    backtrack(remaining_count)
                    remaining_count[letter] += 1

        backtrack(letter_count)
        return self.result

