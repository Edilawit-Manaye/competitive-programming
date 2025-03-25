# Problem: Maximum Score Words Formed by Letters - https://leetcode.com/problems/maximum-score-words-formed-by-letters/description/

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letter_count = Counter(letters)

        def calculate_word_score(word: str) -> int:
            return sum(score[ord(char) - ord('a')] for char in word)

        def backtrack(index: int, current_score: int) -> int:
            if index == len(words):
                return current_score
            
            max_score = backtrack(index + 1, current_score)
            word = words[index]
            word_count = Counter(word)

            can_form = all(letter_count[char] >= word_count[char] for char in word_count)

            if can_form:
                for char in word_count:
                    letter_count[char] -= word_count[char]

                word_score = calculate_word_score(word)
                max_score = max(max_score, backtrack(index + 1, current_score + word_score))

                for char in word_count:
                    letter_count[char] += word_count[char]

            return max_score
        
        return backtrack(0, 0)

